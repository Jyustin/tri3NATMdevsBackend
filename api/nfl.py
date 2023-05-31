from model.nfls import player_list
from flask import Blueprint, Flask, jsonify
from flask_restful import Resource, Api

nfl_api = Blueprint('nfl_api', __name__, url_prefix='/api/nfl')
api = Api(nfl_api)

class NflAPI:
    class Read(Resource):
        def get(self):
            return jsonify(player_list)

    api.add_resource(Read, '/')
