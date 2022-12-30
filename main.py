import os
import json
import datetime
from flask import Flask, render_template

app = Flask(__name__)

BASE_FOLDER = os.path.dirname(os.path.abspath(__file__))
RESOURCE_DIR = os.path.join(BASE_FOLDER, "resources")


@app.route('/')
def hello_world():
    with open(os.path.join(RESOURCE_DIR, "response.json")) as f:
        ip = os.popen('curl ifconfig.me')
        date = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
        version = json.loads(f.read()).get("payload")
        return render_template('index.html', date=date, version=version, ip=ip.read())


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
