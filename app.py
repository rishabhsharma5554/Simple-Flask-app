import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "<h1>Your Application is running Fine............<h1/>"

@app.route('/v1')
def v1App():
    return '<h1>V1 of Application.<h1/>'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000)
