from flask import Flask, render_template, request, jsonify, session
import db_config

app = Flask(__name__)
# Secret Key for session
app.secret_key = 'portofino'


@app.route('/')
def index():
    property_list = db_config.get_all_properties()
    dynamics = {
        "locations": db_config.get_locations(),
        "property_types": db_config.get_property_types(),
        "sale_types": db_config.get_sale_types(),
    }
    return render_template('index.html', dynamics=dynamics, property_list=property_list)


@app.route('/property', methods=['POST'])
def property():
    location = request.form['location_list']
    property_type = request.form['property_types']
    sale_type = request.form['sale_types']
    condition = request.form['condition']
    range_min = float(str(request.form['min_val']).split('L')[0]) * 100000
    range_max = float(str(request.form['max_val']).split('L')[0]) * 100000

    # print(location, property_type,sale_type, condition, range_min, range_max)
    # query = { '$and': [ { "price": { '$gt': range_min} }, { "price": { '$lt': range_max  } }, {"location": location}, {"type": property_type}, {"bedrooms": {'$gte': bed_rooms}}, {"bathrooms": {'$gte': bath_rooms}} ] }
    # result = db_config.collection.find(query)
    property_list = db_config.get_requested_properties(location, property_type, sale_type, range_max, range_min)
    # for x in result:
    #     count += 1
    #     property_list.append(x)



    dynamics = {
        "locations" : db_config.get_locations(),
        "property_types" : db_config.get_property_types(),
        "sale_types" : db_config.get_sale_types(),
    }



    return render_template('property.html', dynamics = dynamics, property_list=property_list)

@app.route('/register_property', methods=['GET', 'POST'])
def register_property():
    dynamics = {
        "locations": db_config.get_locations(),
        "property_types": db_config.get_property_types(),
        "sale_types": db_config.get_sale_types(),
    }
    return render_template("register_property.html", dynamics=dynamics)