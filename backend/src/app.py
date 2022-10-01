from flask import Flask, jsonify

app = Flask(__name__)

# we can avoid using mongo if we use this 
# https://www.geeksforgeeks.org/read-json-file-using-python/

@app.route("/user/<id>")
def userData(id):

    id = str(id).strip()
    return jsonify({
        "username": "john.doe",
        "name": "John Doe",
        "pfp": "http://example.com",
	    "activity_log": [],
	    "wish_list": []
    })
    
@app.route("/popularactivities")
def popularActivities():

    return jsonify({ 
        "id": 123123,
        "name": "Activity name",
        "photo": "http://example.com",
        "location":  "string",
        "location_link": "string",
        "category": "Fun",
        "description": "Sample string",
        "rating": 6,
        "sustainable": True
    })