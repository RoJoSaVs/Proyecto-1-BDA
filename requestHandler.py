# CRUD BACKEND
import flask
from flask import request, jsonify, g, render_template
from flask_cors import CORS, cross_origin
import json
import time
import mongodb

app = flask.Flask(__name__)
CORS(app, support_credentials=True)
test = mongodb.MongoDBHandler("MongoDBA-R", "BDA", "Lab2_BDA")


@app.route('/', methods=['GET'])
def home():
	return render_template('Snake.html')


# A route to return all of the available entries in our catalog.
@app.route('/api/employees', methods=['GET'])
def api_all():
	return jsonify(test.readAllFromMongoDB())

@app.route('/api/single_employees', methods=['GET'])
def api_single_record():
    return jsonify(test.readOneFromMongoDB("Author", "Stephen King"))


@app.route('/api/parse', methods=['POST'])
def parse():
    data = request.json
    filename = data['filename']
    extension = data['extension']
    swear_words = azure_blob_handler.get_blob(filename, extension)
    response = [{'number': swear_words}]
    return jsonify(response)


@app.route('/api/login', methods=['POST', 'GET'])
def login():
    data = request.data
    return (data)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)


app.run()