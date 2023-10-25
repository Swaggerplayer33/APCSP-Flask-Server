from flask import Blueprint, jsonify
from flask_restful import Api, Resource, reqparse
from __init__ import app, db
from model.cars import Cars

car_api = Blueprint('car', __name__, url_prefix='/api/car')
api = Api(car_api)

class CarsResource(Resource):
    def get(self):
        cars = Cars.query.all()
        car_list = [car.alldetails() for car in cars]
        return jsonify(car_list)

class CarDetailsResource(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('id', type=int, required=True)
        super(CarDetailsResource, self).__init__()

    def get(self):
        args = self.parser.parse_args()
        car = Cars.query.get(args['id'])
        if car is None:
            return jsonify({"error": "Car not found"}), 404
        return jsonify(car.alldetails())

api.add_resource(CarsResource, "/cars")
api.add_resource(CarDetailsResource, "/cardetails")
