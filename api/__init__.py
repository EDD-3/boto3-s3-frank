from flask import Flask, render_template, request, jsonify
from ssl import SSLContext
import json
from urllib.request import urlopen
import api.config


app     = Flask(__name__)
app.config.from_object(api.config)

if __name__ == "__main__":
    app.run()

from api.helpers import *

@app.route("/", methods=["GET"])
def index():
    return "Hello"

@app.route("/api/images", methods=["POST"])
def upload_file():
    try:
        file_url = json.loads(request.data)['imageUrl']
        response = urlopen(file_url, context=SSLContext())

        if response.code == 200:
            output = upload_file_to_s3(response)
            return jsonify({ "imageUrl": output }), 200

    except Exception as e:
        return jsonify({'Exception': e}),500

@app.route("/api/images", methods=["GET"])
def get_files():
    try:
        response = get_bucket_files()
        return jsonify(response), 200
    except Exception as e:
        return jsonify({"Exception": e}),500
        