from flask import Flask, jsonify
import database

app = Flask(__name__)

@app.route("/user/<username>")
def userData(username):
    username = username.strip()
    return jsonify(database.getProfileByUsername(username))
    
@app.route("/popularactivities")
def popularActivities():
    return jsonify(database.getAllActivities())