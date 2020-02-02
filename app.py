from flask import Flask, render_template, request, jsonify
import config

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/property', methods=['POST'])
def property():
    location = request.form['location_list']
    property_type = request.form['property_types']
    bed_rooms = str(request.form['bed_rooms'])
    bath_rooms = str(request.form['bath_rooms'])
    range_min = float(request.form['min_val']) * 100000
    range_max = float(request.form['max_val']) * 100000

    print(location, property_type, bed_rooms, bath_rooms, range_min, range_max)
    query = { '$and': [ { "price": { '$gt': range_min} }, { "price": { '$lt': range_max  } }, {"location": location}, {"type": property_type}, {"bedrooms": {'$gte': int(str(request.form['bed_rooms']).split('+')[0])}}, {"bathrooms": {'$gte': int(str(request.form['bath_rooms']).split('+')[0])}} ] }
    result = config.collection.find(query)
    count = 0
    property_list = []
    for x in result:
        count += 1
        property_list.append(x)

    vals = [location, property_type, range_min, range_max, bed_rooms, bath_rooms]

    return render_template('property.html', property_count=count, property_list=property_list, val=vals)


@app.route('/property', methods=['GET'])
def property_get():
    result = config.collection.find()
    count = 0
    property_list = []
    for x in result:
        count += 1
        property_list.append(x)


    return render_template('property.html', property_count=count, property_list=property_list)

