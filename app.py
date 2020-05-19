from flask import Flask, render_template, request, jsonify
from ssl import SSLContext
import json
from urllib.request import urlopen



app     = Flask(__name__)
app.config.from_object("config")

if __name__ == "__main__":
    app.run()
    app.debug = True

from helpers import *

@app.route("/")
def index():
    return render_template("index.html")



@app.route("/images", methods=["POST"])
def upload_file():
    try:
        file_info = json.loads(request.data)
        response = urlopen(file_info['urlImage'], context=SSLContext())

        if response.code == 200:
            output = upload_file_to_s3(response , app.config["S3_BUCKET"])
            return jsonify(output), 200

    except Exception as e:
        return jsonify({'Exception': e}),500