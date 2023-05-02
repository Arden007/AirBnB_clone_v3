#!/usr/bin/python3
"""
index routes for flask
    routes:
        /status:    display "status":"OK"
        /stats:     display count for all classes
"""
from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route("/status")
def status():
    """Returns a JSON response: ("status": "OK")"""
    return jsonify({'status': 'OK'})


@app_views.route("/stats")
def stats_counts():
    """retrieves the number of each objects by type"""
    obj = {
        "amenities": "Amenity",
        "cities": "City",
        "places": "Place",
        "reviews": "Review",
        "states": "State",
        "users": "User"
    }
    for i in obj.keys():
        obj[i] = storage.count(obj.get(i))
    return jsonify(obj)
