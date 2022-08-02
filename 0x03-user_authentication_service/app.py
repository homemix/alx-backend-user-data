#!/usr/bin/env python3
"""
A flask application
"""

from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    """
    return welcome message
    :return:
    """
    return jsonify({"message": "Bienvenue"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
