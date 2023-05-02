#!/usr/bin/python3
""" Set-up of the Api's principal application"""
from flask import Flask, jsonify
from flask_cors import CORS
from models import storage
from os import getenv
from api.v1.views import app_views
from flasgger import Swagger

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "0.0.0.0"}})
app.url_map.strict_slashes = False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.register_blueprint(app_views)
swagger = Swagger(app)


@app.errorhandler(404)
def page_not_found(err):
    return jsonify({"error": "Not found"}), 404


@app.teardown_appcontext
def close(obj):
    storage.close()


if __name__ == "__main__":
    apiHost = getenv("HBNB_API_HOST", default="0.0.0.0")
    apiPort = getenv("HBNB_API_PORT", default=5000)
    app.run(host=apiHost, port=int(apiPort), threaded=True)
