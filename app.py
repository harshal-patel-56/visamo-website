import uuid
import logging
from PIL import Image

from flask import Flask, render_template, request, jsonify, session, url_for, redirect, send_from_directory
import db_config

app = Flask(__name__)
# Secret Key for session
app.secret_key = 'portofino'


# USER_ID = 73


# logger = logging.getLogger()
# hdlr = logging.FileHandler('myapp.log')
# formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
# hdlr.setFormatter(formatter)
# logger.addHandler(hdlr)
# logger.setLevel(logging.ERROR)
#
# @app.errorhandler(Exception)
# def handle_exceptions(e):
#     logger.error(e)
#     return redirect(url_for('index'))
#
# @app.route('/robots.txt')
# def send_file_robots_txt():
#     return send_from_directory('static','robots.txt')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        warning_message = ""
        if 'logged_in' in session:
            return redirect(url_for('index'))
        elif request.args.get('warning_message'):
            warning_message = request.args.get('warning_message')
        return render_template("login.html", warning_message=warning_message)

    if request.method == 'POST':
        username = str(request.form['email'])
        password = str(request.form['password'])
        # print(user_type)
        result = db_config.get_login(username, password)
        if result == 1:
            session['logged_in'] = True
            session['username'] = username.split('@')[0]
            if username == 'admin@visamo.com':
                session['admin'] = 'admin'
            return redirect(url_for('index'))
        elif result == 2:
            return render_template("login.html", warning_message="Incorrect Password")
        else:
            return render_template("login.html", warning_message="User doesn't exist")


@app.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    warning_message = ""
    if request.method == 'GET':
        if 'logged_in' in session:
            return redirect(url_for('index'))
        return render_template("sign_up.html", attendance_list=None, warning_message=warning_message)

    else:

        f_name = str(request.form['f_name'])
        l_name = str(request.form['l_name'])
        # username = str(request.form['username'])
        email = str(request.form['email'])
        contact = str(request.form['contact'])
        pass1 = str(request.form['password'])
        pass2 = str(request.form['password1'])

        if pass1 == pass2:
            if db_config.register_user(pass1, f_name, l_name, contact, email):
                warning_message = "Registered Successfully"
            else:
                warning_message = "User already exists"
        else:
            warning_message = "Password didn't match"
        return render_template("sign_up.html", warning_message=warning_message)


@app.route('/logout', methods=['GET'])
def logout():
    session.pop('logged_in', 0)
    session.pop('username', None)
    session.pop('admin', None)
    return redirect(url_for('login', warning_message='Logged Out'))


@app.route('/')
def index():
    try:
        if 'logged_in' in session:
            property_list = db_config.get_all_properties()
            dynamics = {
                "locations": db_config.get_locations(),
                "property_types": db_config.get_property_types(),
                "sale_types": db_config.get_sale_types(),
            }
            admin = session['admin'] if 'admin' in session else ''
            return render_template('index.html', dynamics=dynamics, property_list=property_list, admin=admin,
                                   username=session['username'])
        else:
            return redirect(url_for('logout'))
    except Exception as e:
        return redirect(url_for('logout'))
        # logger.error(e)
        # pass


@app.route('/properties', methods=['GET', 'POST'])
def properties():
    if 'logged_in' in session:
        if request.method == 'POST':
            location = request.form['location_list']
            property_type = request.form['property_types']
            sale_type = request.form['sale_types']
            condition = request.form['condition']
            range_min = float(str(request.form['min_val']).split('L')[0]) * 100000
            range_max = float(str(request.form['max_val']).split('L')[0]) * 100000
            property_list = db_config.get_requested_properties(location, property_type, sale_type, range_max, range_min)
        else:
            property_list = db_config.get_all_properties()

        # print(property_list)

        dynamics = {
            "locations": db_config.get_locations(),
            "property_types": db_config.get_property_types(),
            "sale_types": db_config.get_sale_types(),
        }
        admin = session['admin'] if 'admin' in session else ''
        return render_template('properties.html', dynamics=dynamics, property_list=property_list, admin=admin,
                               username=session['username'])
    else:
        return redirect(url_for('logout'))


@app.route('/properties_info', methods=['GET'])
def display_property():
    if 'logged_in' in session:

        property_id = request.args.get('p_id')
        property_info = db_config.get_property_info(property_id)
        admin = session['admin'] if 'admin' in session else ''
        return render_template('property_details.html', property_info=property_info, admin=admin,
                               username=session['username'])
    else:
        return redirect(url_for('logout'))


@app.route('/register_property', methods=['GET', 'POST'])
def register_property():
    if 'logged_in' in session:
        dynamics = {
            "locations": db_config.get_locations(),
            "property_types": db_config.get_property_types(),
            "sale_types": db_config.get_sale_types(),
        }

        if request.method == 'GET':
            admin = session['admin'] if 'admin' in session else ''
            return render_template("register_property.html", dynamics=dynamics, admin=admin,
                                   username=session['username'])
        else:
            property_id = uuid.uuid4().hex
            # property_id = 10
            property_name = request.form.get("property_name")
            property_description = request.form.get("property_description")
            address = str(request.form.get("address"))
            price = float(request.form.get("price")) * 100000
            location = request.form.get("location")
            property_type = request.form.get("property_type")
            sale_type = request.form.get("sale_type")
            area = request.form.get("area")
            age = request.form.get("age")
            is_owner = int(1) if request.form.get("is_owner") == 'on' else int(0)
            image_file = request.files['image']
            temp = image_file.filename
            src_path = "static/img/property/" + str(property_id) + "." + temp.split(".")[-1]
            image_file.save(src_path)

            image = Image.open(src_path)
            image = image.resize((362, 240))
            image.save(src_path)

            status_message = ""
            if db_config.insert_property(property_id, session['username'], property_name, property_description, address,
                                         price,
                                         location,
                                         property_type, sale_type, area, age, is_owner, src_path):
                status_message = "Registered Successfully"
            else:
                status_message = "Oops Something went wrong!!!"
            admin = session['admin'] if 'admin' in session else ''
            return render_template("register_property.html", dynamics=dynamics, admin=admin,
                                   status_message=status_message, username=session['username'])
    else:
        return redirect(url_for('logout'))


@app.route('/approval_requests', methods=['GET', 'POST'])
def pending_properties():
    if 'logged_in' in session:
        pending_properties_list = []
        if request.method == 'GET':
            pending_properties_list = db_config.get_pending_properties()
        else:
            dictionary = request.form.to_dict()
            for key in dictionary:
                db_config.approve(key)

            pending_properties_list = db_config.get_pending_properties()
        admin = session['admin'] if 'admin' in session else ''
        return render_template("approval_requests.html", property_list=pending_properties_list, admin=admin,
                               username=session['username'])
    else:
        return redirect(url_for('logout'))
