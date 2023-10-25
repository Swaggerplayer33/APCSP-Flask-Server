# Import necessary Flask and Flask-RESTful modules
from flask import Blueprint, jsonify
from flask_restful import Api, Resource, reqparse

# Import your Flask app and database instance
from __init__ import app, db

# Import the Cars model from your project
from model.cars import Cars

# Create a Blueprint for the car-related API
car_api = Blueprint('car', __name__, url_prefix='/api/car')
api = Api(car_api)

# Define a resource for retrieving a list of all cars
class CarsResource(Resource):
    def get(self):
        # Query the database to get all cars
        cars = db.session.query(Cars).all()
        # Return a JSON response with details for all cars
        return jsonify([car.alldetails() for car in cars])

# Define a resource for retrieving details of a specific car by ID
class CarDetailsResource(Resource):
    def get(self):
        # Use reqparse to parse the 'id' query parameter from the request
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=int)
        args = parser.parse_args()
        
        # Query the database to find the car with the specified ID
        car = db.session.query(Cars).filter(Cars.id == args['id']).first()
        
        # Check if the car is found
        if car:
            # Return a JSON response with details for the specific car
            return jsonify(car.alldetails())
        else:
            # Return a JSON response with an error message and a 404 status code if the car is not found
            return jsonify({'error': 'Car not found'}), 404

# Add the CarsResource and CarDetailsResource to the Flask-RESTful API
api.add_resource(CarsResource, '/cars')
api.add_resource(CarDetailsResource, '/cardetails')
