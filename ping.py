import http
import time
from flask import Flask, jsonify, request
from flask_httpauth import HTTPDigestAuth
import requests


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret key here'
auth = HTTPDigestAuth()

users = {
    'vcu': 'rams'
}


@auth.get_password
def get_pw(username):
    if username in users:
        return users.get(username)
    return None


@app.route('/ping', methods=['GET'])
@auth.login_required
def ping():
    start = time.perf_counter()
    response = requests.get("http://127.0.0.1:5000/pong")
    request_time = time.perf_counter() - start
    return "Request completed in {0:.0f}ms".format(request_time)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
