from flask import Flask, request, render_template, send_file
from werkzeug.exceptions import NotFound, BadRequest
from os.path import isfile
from bjoern import run
from threading import Thread
from pull_edt import pull

app = Flask(__name__)


ELEMENTS = [
    {
        "name": "German_Holidays",
        "url": "https://www.calendarlabs.com/ical-calendar/ics/46/Germany_Holidays.ics"
    }
]

Thread(target=pull, args=(ELEMENTS,)).start()


@app.route('/')
def list_edt():
    return render_template("index.j2", elements=ELEMENTS)


@app.route("/edt/")
def show_edt():
    group = request.args.get("group")
    if group is None:
        raise BadRequest
    if isfile("ics/" + group + ".ics"):
        return render_template("edt.j2", group=group)
    raise NotFound


@app.route("/ics/")
def get_ics():
    file = request.args.get("file")
    if file is None:
        raise BadRequest
    path = "ics/" + file + ".ics"
    if isfile(path):
        return send_file(path)
    raise NotFound


if __name__ == '__main__':
    run(app, port=9586, host="0.0.0.0")
