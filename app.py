from flask import Flask, render_template, request, jsonify, session
import db_config

app = Flask(__name__)
# Secret Key for session
app.secret_key = 'portofino'


@app.route('/')
def index():
    locations = db_config.get_locations()
    property_types = db_config.get_property_types()
    sale_types = db_config.get_sale_types()
    return render_template('index.html', locations=locations, property_types=property_types, sale_types=sale_types)


@app.route('/property', methods=['POST'])
def property():
    location = request.form['location_list']
    property_type = request.form['property_types']
    sale_type = request.form['sale_types']
    condition = request.form['condition']
    range_min = float(str(request.form['min_val']).split('L')[0]) * 100000
    range_max = float(str(request.form['max_val']).split('L')[0]) * 100000

    print(location, property_type,sale_type, condition, range_min, range_max)
    # query = { '$and': [ { "price": { '$gt': range_min} }, { "price": { '$lt': range_max  } }, {"location": location}, {"type": property_type}, {"bedrooms": {'$gte': bed_rooms}}, {"bathrooms": {'$gte': bath_rooms}} ] }
    # result = db_config.collection.find(query)
    count = 0
    property_list = []
    # for x in result:
    #     count += 1
    #     property_list.append(x)

    return render_template('property.html')

