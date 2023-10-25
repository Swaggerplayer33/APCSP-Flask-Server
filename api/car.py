<<<<<<< HEAD
from flask import Blueprint, jsonify
from flask_restful import Api, Resource, reqparse
from __init__ import app, db
from model.ownCarsAPI import Cars

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
=======
import requests

url = "https://cars-by-api-ninjas.p.rapidapi.com/v1/cars"

modelInput = str(input("What is your car model: "))
querystring = {"model": modelInput}

headers = {
    "X-RapidAPI-Key": "a8491de794msh6676acc5521c4fcp1c5cf8jsn6d99a8656992",
    "X-RapidAPI-Host": "cars-by-api-ninjas.p.rapidapi.com"
}

def get_car_info():
    response = requests.get(url, headers=headers, params=querystring)
    return response

response = get_car_info()

if response.status_code == 200:
    car_data = response.json()
    print("Car Information:")
    print(car_data)
else:
    print("Error:", response.status_code, response.text)

>>>>>>> e03120cda7f9eb62c066f8985fa46dbf2fae784a
