from flask import Flask
app = Flask(__name__)

@app.route("/")
def welcome():
    return("Welcome to Flask Code ")

@app.route("/home")
def home():
    return("Welcome to Home Page ")

@app.route("/service")
def service():
    return("Welcome to Service Page ")

@app.route("/test1")
def test1():
    return("Welcome to Test 1")