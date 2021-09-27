# CRUD BACKEND
import flask
from flask import request, jsonify, g, render_template
from flask_cors import CORS, cross_origin
import json
import time
import mongodb
import sys

app = flask.Flask(__name__)
CORS(app, support_credentials=True)
mongo_database = mongodb.MongoDBHandler("MongoDBA-R", "BDA", "Lab2_BDA")


@app.route('/', methods=['GET'])
def home():
	return render_template('Snake.html')



# A route to return all of the available entries in our catalog.
@app.route('/api/employees', methods=['GET'])
def api_all():
	return jsonify(mongo_database.readAllFromMongoDB())



@app.route('/api/single_employee', methods=['GET'])
def api_single_record():
    request_param = list(request.args.keys())[0]
    request_value = request.args.get(request_param)
    return jsonify(mongo_database.readOneFromMongoDB(request_param, request_value))



@app.route('/api/add_employee', methods=['POST'])
def add_single_record():
    data = request.json
    # print(data["Name"], file=sys.stderr)
    # filename = data['filename']
    # extension = data['extension']
    # response = [{'number': swear_words}]
    # return data
    return jsonify(mongo_database.insertToMongoDB(data))



@app.route('/api/edit_employee', methods=['PUT'])
def edit_single_record():
    request_param = list(request.args.keys())[0]
    request_value = request.args.get(request_param)
    data = request.json
    return jsonify(mongo_database.updateToMongoDB(request_param, request_value, data))
    # filename = data['filename']
    # extension = data['extension']
    # response = [{'number': swear_words}]
    # return jsonify(response)



@app.route('/api/delete_employee', methods=['DELETE'])
def delete_single_record():
    request_param = list(request.args.keys())[0]
    request_value = request.args.get(request_param)
    return jsonify(mongo_database.deleteToMongoDB(request_param, request_value))




@app.route('/api/login', methods=['POST', 'GET'])
def login():
    data = request.data
    return (data)




if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

app.run()