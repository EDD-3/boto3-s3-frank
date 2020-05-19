from flask import Flask, render_template, request, redirect, flash, url_for,jsonify
from ssl import SSLContext
from werkzeug import secure_filename
import json
from urllib.request import urlopen



app     = Flask(__name__)
app.config.from_object("config")


from helpers import *


@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run()
    app.debug = True

@app.route("/images", methods=["POST"])
def upload_file():
    file_info = json.loads(request.data)
    if file_info and file_info['urlImage']:
        response = urlopen(file_info['urlImage'], context=SSLContext())
        if response.code == 200:
            output = upload_file_to_s3(response , app.config["S3_BUCKET"])
            return jsonify({"imageUrl": output}), 200
    else:
        return redirect("/")