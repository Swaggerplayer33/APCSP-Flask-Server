from flask import Blueprint, jsonify  # jsonify creates an endpoint response object
from flask_restful import Api, request, Resource # used for REST API building
import requests  # used for testing
import random
from __init__ import app, db
from model.cars import Cars

car_api = Blueprint('car', __name__, url_prefix='/api/car')
# API generator https://flask-restful.readthedocs.io/en/latest/api.html#id1


api = Api(car_api)
class cars:
    class _getCars(Resource):
        def get(self):
            cars = db.session.query(Cars).all()
            return jsonify([cars.alldetails() for car in cars])
        
    class _getcardetails(Resource):
        def get(self):
            car = db.session.query(Cars).filter(Cars.id == int(request.args.get("id"))).first()
            return jsonify(car.alldetails())
    
    api.add_resource(_getCars, "/cars")
    api.add_resource(_getcardetails, "/cardetails")