from flask import Flask, request, render_template, send_file
from werkzeug.exceptions import NotFound
from os.path import isfile
from bjoern import run

app = Flask(__name__)


ELEMENTS = [
    {
        "name": "TP2A",
        "url": "google.fr"
    }
]


@app.route('/')
def list_edt():
    print(request.path)
    return render_template("index.j2", elements=ELEMENTS)


@app.route("/edt/")
def show_edt():
    return "gégé"


@app.route("/ics/")
def get_ics():
    path = "ics/" + request.args.get("file")
    if isfile(path):
        return send_file(path)
    else:
        raise NotFound


if __name__ == '__main__':
    run(app, port=9586, host="0.0.0.0")
