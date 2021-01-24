from flask import Flask, jsonify, request
from flask_restful import Api, Resource

from pymongo import MongoClient

app = Flask(__name__)
api = Api(app)

client = MongoClient("mongodb://db:27017")
db = client.aNewDb
UserNum = db["UserNum"]
UserNum.insert({
    'num_of_users': 0
})

class Visit(Resource):
    def get(self):
        prev_num = UserNum.find({})[0]['num_of_users']
        new_num = prev_num + 1
        UserNum.update({}, {'$set':{'num_of_users':new_num}})
        return str("Hello user " + str(new_num))

def checkPostedData(postedData, functionName):
    if "x" not in postedData or "y" not in postedData:
        return 301, "You must send x and y"
    if functionName == 'add':
        return 200, "Ok"
    elif functionName == 'division':
        if postedData["y"] == 0:
            return 302, "0 can't be in division field"
        return 200, "Ok"
class Add(Resource):
    def post(self):
        postedData = request.get_json()
        status_code, message = checkPostedData(postedData, "add")
        if status_code != 200:
            return jsonify({ "Message" : message, 'Status Code':status_code})
        x = int(postedData["x"])
        y = int(postedData["y"])
        return jsonify({ "Message" : x + y, 'Status Code':status_code})
    def get(self):
        pass
    def put(self):
        pass
    def delete(self):
        pass

class Subtract(Resource):
    def post(self):
        postedData = request.get_json()
        status_code, message = checkPostedData(postedData, "add")
        if status_code != 200:
            return jsonify({ "Message" : message, 'Status Code':status_code})
        x = int(postedData["x"])
        y = int(postedData["y"])
        return jsonify({ "Message" : x - y, 'Status Code':status_code})
    def get(self):
        pass
    def put(self):
        pass
    def delete(self):
        pass

class Multiply(Resource):
    pass

class Division(Resource):
    def post(self):
        postedData = request.get_json()
        status_code, message = checkPostedData(postedData, "division")
        if status_code != 200:
            return jsonify({ "Message" : message, 'Status Code':status_code})
        x = int(postedData["x"])
        y = int(postedData["y"])
        return jsonify({ "Message" : x / y, 'Status Code':status_code})
    def get(self):
        pass
    def put(self):
        pass
    def delete(self):
        pass 

api.add_resource(Add, "/add")
api.add_resource(Subtract, "/subtract")
api.add_resource(Division, "/division")
api.add_resource(Visit, "/hello")



@app.route('/')
def hello_would():
    return "Hello World!"

@app.route('/info')
def info():
    retJson = {
        'field1' : 'abc',
        'field2' : 123
    }
    return jsonify(retJson)

@app.route('/add_two_numbers', methods=["POST"])
def add_two_numbers():
    dataDict = request.get_json()
    if "y" not in dataDict:
        return "ERROR", 305

    x = dataDict["x"]
    y = dataDict["y"]
    retJson = {
        'z' : x + y,
    }
    return jsonify(retJson), 201


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)