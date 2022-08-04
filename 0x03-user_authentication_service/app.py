#!/usr/bin/env python3
"""
A flask application
"""

from auth import Auth
from flask import abort, Flask, jsonify, request

app = Flask(__name__)
AUTH = Auth()


@app.route('/')
def index():
    """
    return welcome message
    :return:
    """
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'])
def users():
    """
    register new user
    :return:
    """
    email = request.form.get('email')
    password = request.form.get('password')

    try:
        AUTH.register_user(email=email, password=password)
        return jsonify({"email": email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'])
def login():
    """
    login user
    :return:
    """
    try:
        email = request.form['email']
        password = request.form['password']
    except KeyError:
        abort(400)

    if not AUTH.valid_login(email, password):
        abort(401)

    session_id = AUTH.create_session(email)

    response = jsonify({"email": email, "message": "logged in"})

    response.set_cookie("session_id", session_id)

    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
