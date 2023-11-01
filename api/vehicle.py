from flask import Blueprint, jsonify
from flask_restful import Api, Resource

vehicles_api = Blueprint('vehicles_api', __name__, url_prefix='/api/vehicles')

api = Api(vehicles_api)

# Initialize a list to store vehicle data with likes and dislikes
vehicles = [
    {
        "make": "Bugatti",
        "model": "Chiron",
        "likes": 0,
        "dislikes": 0,
    },
    {
        "make": "Tesla",
        "model": "Roadster",
        "likes": 0,
        "dislikes": 0,
    },
    {
        "make": "Rolls Royce",
        "model": "Phantom",
        "likes": 0,
        "dislikes": 0,
    },
    {
        "make": "Mercedes Benz",
        "model": "G Class",
        "likes": 0,
        "dislikes": 0,
    },
    {
        "make": "Aston Martin",
        "model": "DB11",
        "likes": 0,
        "dislikes": 0,
    },
    {
        "make": "Ferrari",
        "model": "488GTB",
        "likes": 0,
        "dislikes": 0,
    },
    {
        "make": "Bentley",
        "model": "Continental GT",
        "likes": 0,
        "dislikes": 0,
    },
    {
        "make": "Porsche",
        "model": "911 Targa",
        "likes": 0,
        "dislikes": 0,
    },
    {
        "make": "McLaren",
        "model": "720 S",
        "likes": 0,
        "dislikes": 0,
    },
    {
        "make": "Maserati",
        "model": "Quattroporte",
        "likes": 0,
        "dislikes": 0,
    },
    {
        "make": "Audi",
        "model": "R8 Spyder",
        "likes": 0,
        "dislikes": 0,
    },
    {
        "make": "Mercedes Benz",
        "model": "300 SL Gullwing",
        "likes": 0,
        "dislikes": 0,
    },
    {
        "make": "Ferrari",
        "model": "250 GT California",
        "likes": 0,
        "dislikes": 0,
    },
    {
        "make": "Bentley",
        "model": "Flying Spur",
        "likes": 0,
        "dislikes": 0,
    },
    {
        "make": "Audi",
        "model": "A8",
        "likes": 0,
        "dislikes": 0,
    },
    {
        "make": "Jaguar",
        "model": "F-Type",
        "likes": 0,
        "dislikes": 0,
    },
    {
        "make": "Lamborghini",
        "model": "Huracan",
        "likes": 0,
        "dislikes": 0,
    },
    {
        "make": "Rivian",
        "model": "R1S",
        "likes": 0,
        "dislikes": 0,
    },
    {
        "make": "Mercedes Benz",
        "model": "Maybach S Class",
        "likes": 0,
        "dislikes": 0,
    },
    {
        "make": "BMW",
        "model": "7 Series",
        "likes": 0,
        "dislikes": 0,
    },
    {
        "make": "Lincoln",
        "model": "Continental",
        "likes": 0,
        "dislikes": 0,
    },
    {
        "make": "Tesla",
        "model": "Cybertruck",
        "likes": 0,
        "dislikes": 0,
    },
    {
        "make": "Lamborghini",
        "model": "Urus",
        "likes": 0,
        "dislikes": 0,
    },
]

class VehiclesAPI:
    class _Read(Resource):
        def get(self):
            sorted_vehicles = sorted(vehicles, key=lambda vehicle: vehicle["likes"] - vehicle["dislikes"], reverse=True)
            return jsonify(sorted_vehicles)

    class _Like(Resource):
        def post(self, make, model):
            vehicle = next((v for v in vehicles if v["make"] == make and v["model"] == model), None)
            if vehicle:
                vehicle["likes"] += 1
                return "Liked!"
            return "Vehicle not found", 404

    class _Dislike(Resource):
        def post(self, make, model):
            vehicle = next((v for v in vehicles if v["make"] == make and v["model"] == model), None)
            if vehicle:
                vehicle["dislikes"] += 1
                return "Disliked!"
            return "Vehicle not found", 404

api.add_resource(VehiclesAPI._Read, '/')
api.add_resource(VehiclesAPI._Like, '/like/<string:make>/<string:model>')
api.add_resource(VehiclesAPI._Dislike, '/dislike/<string:make>/<string:model>')

if __name__ == "__main__":
    from flask import Flask
    app = Flask(__name__)
    app.register_blueprint(vehicles_api)
    app.run(debug=True, host="0.0.0.0", port=8420)
