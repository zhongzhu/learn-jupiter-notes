from flask import Flask
app = Flask(__name__)

users = {'zhongzhu': '18'}

@app.route("/user/<string:username>")
def sayhello(username):
    return "Hello " + username

@app.route("/user/<string:username>/age")
def hello(username):
    return "Hello " + username + ' age: ' + users[username]