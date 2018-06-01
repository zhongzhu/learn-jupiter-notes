from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/onelab/api/v1.0/user/<username>/profile')
def profile(username):
    id, email, site = [123, 'happy@haha.com', 'Beijing']
    return jsonify(result={'id':id, 'name':username,'email':email, 'site':site})



