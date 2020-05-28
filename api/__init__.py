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
        file_info = json.loads(request.data)
        response = urlopen(file_info['imageUrl'], context=SSLContext())

        if response.code == 200:
            output = upload_file_to_s3(response , app.config["S3_BUCKET"])
            return jsonify({ "imageUrl": output }), 200

    except Exception as e:
        return jsonify({'Exception': e}),500

@app.route("/api/images", methods=["GET"])
def get_files():
    try:
        pass
    except Exception as e:
        pass
    finally:
        pass