# CRUD BACKEND
import flask
from flask import request, jsonify, g, render_template, abort
from flask_cors import CORS, cross_origin
import json
import mongodb
import sys

app = flask.Flask(__name__)
CORS(app, support_credentials=True)
mongo_database = mongodb.MongoDBHandler("MongoDBA-R", "Nodo_R", "Employees")


@app.route('/', methods=['GET'])
def home():
    try:
        return render_template('Snake.html')
    except:
        abort(404)


# A route to return all of the available entries in our catalog.
@app.route('/api/employees', methods=['GET'])
def api_all():
    try:
        return jsonify(mongo_database.readAllFromMongoDB())
    except:
        abort(404)



@app.route('/api/single_employee', methods=['GET'])
def api_single_record():
    try:
        request_param = list(request.args.keys())[0]
        request_value = request.args.get(request_param)
        return jsonify(mongo_database.readOneFromMongoDB(request_param, request_value))
    except:
        abort(404)



@app.route('/api/add_employee', methods=['POST'])
def add_single_record():
    try:
        data = request.json
        request_value = data['email']
        response = mongo_database.readOneFromMongoDB('email', request_value)
        if (response == None):
            return jsonify(mongo_database.insertToMongoDB(data))
        else:
            return jsonify(-1)
    except:
        abort(404)


@app.route('/api/edit_employee', methods=['PUT'])
def edit_single_record():
    try:
        request_param = list(request.args.keys())[0]
        request_value = request.args.get(request_param)
        data = request.json
        return jsonify(mongo_database.updateToMongoDB(request_param, request_value, data))
    except:
        abort(404)



@app.route('/api/delete_employee', methods=['DELETE'])
def delete_single_record():
    try:
        request_param = list(request.args.keys())[0]
        request_value = request.args.get(request_param)
        return jsonify(mongo_database.deleteToMongoDB(request_param, request_value))
    except:
        abort(404)


@app.route('/api/query1', methods=['GET'])
def query1():
    try:
        return jsonify(mongo_database.readMultiFromMongoDB("ti_area", True))
    except:
        abort(404)



@app.route('/api/query2', methods=['GET'])
def query2():
    try:
        return jsonify(mongo_database.readMultiFromMongoDB("languajes.english", "advance"))
    except:
        abort(404)



@app.route('/api/query3', methods=['GET'])
def query3():
    try:
        return jsonify(mongo_database.readMultiFromMongoDB("ti_area", False))
    except:
        abort(404)



@app.route('/login', methods=['POST'])
def login():
    try:
        data = request.json
        request_value = data['email']
        request_password = data['password']
        result = mongo_database.readOneFromMongoDB("email", request_value)
        if ((result != None) and (result['password'] == request_password)):
            if ("admin" in result):
                if (result['admin']):
                    return jsonify('admin')
            else:
                return jsonify('Employee')
        else:
            return jsonify(False)
    except:
        abort(404)



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

app.run()