from flask import Blueprint, jsonify, request
from flask_restful import Api, Resource, reqparse, inputs
from model.players import Player

# Define a more descriptive name for the blueprint and API
player_blueprint = Blueprint('player_blueprint', __name__, url_prefix='/api/players')
api = Api(player_blueprint)

# Define a more specific class name and separate resources for different actions
class PlayerResource(Resource):
    def __init__(self):
        # Use RequestParser for better validation and error handling
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('name', type=str, required=True, help='Name cannot be blank', location='json')
        self.reqparse.add_argument('uid', type=str, required=True, help='UID cannot be blank', location='json')
        self.reqparse.add_argument('password', type=str, location='json')
        self.reqparse.add_argument('tokens', type=int, location='json')
        super(PlayerResource, self).__init__()

    def post(self):
        args = self.reqparse.parse_args()
        # Check for name length
        if len(args['name']) < 2:
            return {'message': 'Name must be at least 2 characters long'}, 400

        # Check for UID length
        if len(args['uid']) < 2:
            return {'message': 'UID must be at least 2 characters long'}, 400
        
        # Create player object
        player = Player(name=args['name'], uid=args['uid'], tokens=args['tokens'])
        if args['password']:
            player.set_password(args['password'])
        
        # Save to database
        created_player = player.create()
        if created_player:
            return jsonify(player.read())
        
        return {'message': f'Error processing {args["name"]}. UID {args["uid"]} might be duplicate'}, 400

    def get(self):
        players = Player.query.all()
        return jsonify([player.read() for player in players])

    def put(self):
        args = self.reqparse.parse_args()
        player = Player.query.get(args['uid'])
        if player:
            player.update(args)
            return f"{player.read()} Updated"
        return {'message': 'Player not found'}, 404

    def delete(self):
        args = self.reqparse.parse_args()
        player = Player.query.get(args['uid'])
        if player:
            player.delete()
            return f"{player.read()} Has been deleted"
        return {'message': 'Player not found'}, 404


api.add_resource(PlayerResource, '/')
