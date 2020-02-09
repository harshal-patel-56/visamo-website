import uuid
from PIL import Image

from flask import Flask, render_template, request, jsonify, session
import db_config

app = Flask(__name__)
# Secret Key for session
app.secret_key = 'portofino'
ADMIN_NAME='admin'
USER_ID = 69

@app.route('/')
def index():
    property_list = db_config.get_all_properties()
    dynamics = {
        "locations": db_config.get_locations(),
        "property_types": db_config.get_property_types(),
        "sale_types": db_config.get_sale_types(),
    }
    return render_template('index.html', dynamics=dynamics, property_list=property_list, admin=ADMIN_NAME)


@app.route('/properties', methods=['GET','POST'])
def properties():
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
        "locations" : db_config.get_locations(),
        "property_types" : db_config.get_property_types(),
        "sale_types" : db_config.get_sale_types(),
    }

    return render_template('properties.html', dynamics = dynamics, property_list=property_list, admin=ADMIN_NAME)

@app.route('/properties_info', methods=['GET'])
def display_property():
    property_id = request.args.get('p_id')
    property_info = db_config.get_property_info(property_id)

    return render_template('property_details.html',property_info=property_info, admin=ADMIN_NAME)


@app.route('/register_property', methods=['GET', 'POST'])
def register_property():
    dynamics = {
        "locations": db_config.get_locations(),
        "property_types": db_config.get_property_types(),
        "sale_types": db_config.get_sale_types(),
    }
    if request.method == 'GET':
        return render_template("register_property.html", dynamics=dynamics, admin=ADMIN_NAME)
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
        if db_config.insert_property(property_id, USER_ID, property_name, property_description, address, price, location,
                        property_type, sale_type, area, age, is_owner, src_path):
            status_message = "Registered Successfully"
        else:
            status_message = "Oops Something went wrong!!!"
        return render_template("register_property.html", dynamics=dynamics, admin=ADMIN_NAME, status_message=status_message)

@app.route('/approval_requests', methods=['GET', 'POST'])
def pending_properties():
    pending_properties_list = []
    if request.method == 'GET':
        pending_properties_list = db_config.get_pending_properties()
    else:
        dictionary = request.form.to_dict()
        for key in dictionary:
            db_config.approve(key)

        pending_properties_list = db_config.get_pending_properties()
    return render_template("approval_requests.html", property_list=pending_properties_list, admin=ADMIN_NAME)