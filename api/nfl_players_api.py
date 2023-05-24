from flask import Blueprint, request, jsonify, make_response
from flask_restful import Api, Resource
from model.nfl_players_model import NFLPlayer

nflplayers_api = Blueprint('nflplayers_api', __name__, url_prefix='/api/nflplayer')

@nflplayers_api.after_request
def after_request(response):
    header = response.headers
    header['Access-Control-Allow-Origin'] = '*'
    header['Access-Control-Allow-Headers'] = "*"
    header['Access-Control-Allow-Methods'] = "*"
    return response

api = Api(nflplayers_api)

class NFLPlayerAPI:
    class _Create(Resource):
        def post(self):
            body = request.get_json()
            player_name = body.get('player_name')
            team = body.get('team')
            position = body.get('position')
            college = body.get('college')
            jersey_number = body.get('jersey_number')
            height = body.get('height')
            weight = body.get('weight')
            # Create NFLPlayer object
            player = NFLPlayer(
                player_name=player_name,
                team=team,
                position=position,
                college=college,
                jersey_number=jersey_number,
                height=height,
                weight=weight
            )
            # Create NFL player in the database
            created_player = player.create()
            if created_player:
                return jsonify(created_player.read())
            return {'message': 'NFL player not created'}, 210

    class _Update(Resource):
        def put(self):
            body = request.get_json()
            player_id = body.get('id')
            # Validate if player exists by ID
            player = NFLPlayer.get_player_by_id(player_id)
            if player is None:
                return {'message': f'NFL player with ID: ({player_id}) not found.'}, 210
            player_name = body.get('player_name')
            team = body.get('team')
            position = body.get('position')
            college = body.get('college')
            jersey_number = body.get('jersey_number')
            height = body.get('height')
            weight = body.get('weight')
            # Update NFLPlayer object
            player.player_name = player_name
            player.team = team
            player.position = position
            player.college = college
            player.jersey_number = jersey_number
            player.height = height
            player.weight = weight
            # Update NFL player in the database
            updated_player = player.update()
            if updated_player:
                return jsonify(updated_player.read())
            return {'message': f'NFL player not updated'}, 210

    class _Read(Resource):
        def get(self):
            player_id = request.args.get("id")
            if player_id:
                player = NFLPlayer.get_player_by_id(player_id)
                if player is None:
                    return {'message': f'NFL player with ID: ({player_id}) not found.'}, 210
                return jsonify(player.read())
            else:
                players = NFLPlayer.query.all()
                json_ready = [player.read() for player in players]
                response = make_response(jsonify(json_ready), 200)
                return response

    class _Delete(Resource):
        def delete(self):
            player_id = request.args.get("id")
            if player_id == "":
                return {'message': f'NFL player ID not provided.'}, 210
            else:
                player = NFLPlayer.get_player_by_id(player_id)
                if player is None:
                    return {'message': f'NFL player with ID: ({player_id}) not found.'}, 210
                player_name = player.player_name
                NFLPlayer.delete(player)
                return {'message': f'NFL player \'{player_name}\' ({player_id}) deleted.'}, 200

    api.add_resource(_Create, '/create')
    api.add_resource(_Delete, '/delete')
    api.add_resource(_Update, '/update')
    api.add_resource(_Read, '/')

### Complete API