from flask import Blueprint, jsonify, request
from flask_restful import Api, Resource, reqparse
from __init__ import db
from model.cars import Cars  # Import the car model

# Create a Blueprint for the car API
car_api = Blueprint('car_api', __name__, url_prefix='/api/car')

# Create the API instance
api = Api(car_api)

class CarAPI:
    class _Create(Resource):
        def post(self):
            # Get request JSON data
            data = request.get_json()

            # Extract car information
            make = data.get('make')
            model = data.get('model')
            year = data.get('year')
            fuel = data.get('fuel')
            cylinders = data.get('cylinders')

            # Create a new car object
            car = Cars(make=make, model=model, year=year, fuel=fuel, cylinders=cylinders)

            try:
                # Add car to the database
                car.create()
                # Return the created car as JSON
                return jsonify(car.alldetails()), 201  # HTTP status 201 (Created)
            except:
                return {'message': 'Invalid input, correct fields should be make, model, year, trim, and cylinders'}, 400

    class _Read(Resource):
        def get(self):
            # Retrieve all cars from the database
            cars = Cars.query.all()
            json_ready = [car.alldetails() for car in cars]
            # Return the JSON response
            return jsonify(json_ready)

    # Define API routes
    api.add_resource(_Create, '/create')
    api.add_resource(_Read, '/')
