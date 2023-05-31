from flask import Blueprint, request, jsonify, make_response
from flask_restful import Api, Resource
from models.premierleagueplayer_model import PremierLeaguePlayer

premierleagueplayers_api = Blueprint('premierleagueplayers_api', __name__, url_prefix='/api/premierleagueplayer')

@premierleagueplayers_api.after_request
def after_request(response):
    header = response.headers
    header['Access-Control-Allow-Origin'] = '*'
    header['Access-Control-Allow-Headers'] = "*"
    header['Access-Control-Allow-Methods'] = "*"
    return response

api = Api(premierleagueplayers_api)

class PremierLeaguePlayerAPI:
    class _Create(Resource):
        def post(self):
            body = request.get_json()
            name = body.get('name')
            team = body.get('team')
            position = body.get('position')
            jersey_number = body.get('jersey_number')
            age = body.get('age')
            # Create PremierLeaguePlayer object
            player = PremierLeaguePlayer(
                name=name,
                team=team,
                position=position,
                jersey_number=jersey_number,
                age=age
            )
            # Create Premier League player in the database
            created_player = player.create()
            if created_player:
                return jsonify(created_player.read())
            return {'message': 'Premier League player not created'}, 210

    class _Update(Resource):
        def put(self):
            body = request.get_json()
            player_id = body.get('id')
            # Validate if player exists by ID
            player = PremierLeaguePlayer.get_player_by_id(player_id)
            if player is None:
                return {'message': f'Premier League player with ID: ({player_id}) not found.'}, 210
            name = body.get('name')
            team = body.get('team')
            position = body.get('position')
            jersey_number = body.get('jersey_number')
            age = body.get('age')
            # Update PremierLeaguePlayer object
            player.name = name
            player.team = team
            player.position = position
            player.jersey_number = jersey_number
            player.age = age
            # Update Premier League player in the database
            updated_player = player.update()
            if updated_player:
                return jsonify(updated_player.read())
            return {'message': f'Premier League player not updated'}, 210

    class _Read(Resource):
        def get(self):
            player_id = request.args.get("id")
            if player_id:
                player = PremierLeaguePlayer.get_player_by_id(player_id)
                if player is None:
                    return {'message': f'Premier League player with ID: ({player_id}) not found.'}, 210
                return jsonify(player.read())
            else:
                players = PremierLeaguePlayer.query.all()
                json_ready = [player.read() for player in players]
                response = make_response(jsonify(json_ready), 200)
                return response

    class _Delete(Resource):
        def delete(self):
            player_id = request.args.get("id")
            if player_id == "":
                return {'message': f'Premier League player ID not provided.'}, 210
            else:
                player = PremierLeaguePlayer.get_player_by_id(player_id)
                if player is None:
                    return {'message': f'Premier League player with ID: ({player_id}) not found.'}, 210
                name = player.name
                PremierLeaguePlayer.delete(player)
                return {'message': f'Premier League player \'{name}\' ({player_id}) deleted.



api.add_resource(_Create, '/create')
api.add_resource(_Delete, '/delete')
api.add_resource(_Update, '/update')
api.add_resource(_Read, '/')