from flask import Flask, request, render_template, send_file
from flask_cors import CORS
from werkzeug.exceptions import NotFound, BadRequest
from os.path import isfile
from bjoern import run
from requests import get

app = Flask(__name__)
CORS(app)


ELEMENTS = [
    {
        "name": "TP2A",
        "url": ""
    }
]


@app.route('/')
def list_edt():
    return render_template("index.j2", elements=ELEMENTS)


@app.route("/edt/")
def show_edt():
    group = request.args.get("group")
    if group == None:
        raise BadRequest
    if isfile("ics/" + group + ".ics"):
        return render_template("edt.j2", group=group)
    raise NotFound


@app.route("/ics/")
def get_ics():
    file = request.args.get("file")
    if file == None:
        raise BadRequest
    path = "ics/" + file + ".ics"
    if isfile(path):
        return send_file(path)
    raise NotFound


if __name__ == '__main__':
    run(app, port=9586, host="0.0.0.0")
