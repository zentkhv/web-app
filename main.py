import os
import json
import datetime
from flask import Flask, render_template

import config

app = Flask(__name__)

BASE_FOLDER = os.path.dirname(os.path.abspath(__file__))
RESOURCE_DIR = os.path.join(BASE_FOLDER, "resources")


@app.route('/')
def home():
    with open(os.path.join(RESOURCE_DIR, "response.json")) as f:
        ip = os.popen('hostname -I')
        version = json.loads(f.read()).get("payload")
        return render_template('index.html', date=config.now_date_time, version=version, ip=ip.read())


if __name__ == "__main__":
    app.run(host=config.local_address, port=config.local_port, debug=True)
