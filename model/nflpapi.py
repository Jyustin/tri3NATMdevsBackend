from flask import Blueprint, request, jsonify, make_response
from flask_restful import Api, Resource # used for REST API building
from datetime import datetime
from model.nflteam import NFLTeam


# create the REST API URI
nflteam_api = Blueprint('nflteam_api', __name__, url_prefix='/api/nflteam')


# add cors headers
@nflteam_api.after_request
def after_request(response):
    header = response.headers
    header['Access-Control-Allow-Origin'] = '*'
    header['Access-Control-Allow-Headers']= "*"
    header['Access-Control-Allow-Methods'] ="*"
    return response


# API docs https://flask-restful.readthedocs.io/en/latest/api.html
api = Api(nflteam_api)


# NFL Team API
class nflteamAPI:
    # Create (Post) method
    class _Create(Resource):
        # Post method
        def post(self):
            ''' Read data for json body '''
            body = request.get_json()
            # Read team data from the body
            team = body.get('team')
            pointsfor = body.get('pointsfor')
            pointsagainst = body.get('pointsagainst')
            playoffs = body.get('playoffs')
            gameswonaway = body.get('gameswonaway')
            gameswonathome = body.get('gameswonathome')
            gameswon = body.get('gameswon')
            gamesplayedaway = body.get('gamesplayedaway')
            gamesplayedathome = body.get('gamesplayedathome')
            gamesplayed = body.get('gamesplayed')
            gameslostaway = body.get('gameslostaway')
            gameslostathome = body.get('gameslostathome')
            gameslost = body.get('gameslost')
            gamesdrawn = body.get('gamesdrawn')
            division = body.get('division')
            # create team object
            teamObj = NFLTeam(division=division, team=team, gamesplayed=gamesplayed, gameswon=gameswon, gameslost=gameslost, gamesdrawn=gamesdrawn, gamesplayedathome=gamesplayedathome, gamesplayedaway=gamesplayedaway, gameswonathome=gameswonathome, gameslostathome=gameslostathome, gameswonaway=gameswonaway, gameslostaway=gameslostaway, gamesplayed5=0, gameswon5=0, gameslost5=0, pointsfor=pointsfor, pointsagainst=pointsagainst,  playoffs=playoffs)
           
            # create nfl team object in database
            nflteam = teamObj.create()
            # success returns json of nfl news
            if nflteam:
                return jsonify(nflteam.read())
            # failure returns error
            return {'message': f'NFL Team not created'}, 210
    # Update (PUT)
    class _Update(Resource):
        # PUT Method
        def put(self):
            ''' Read data for json body '''
            body = request.get_json()
            print(body)
            # Read team data from body
            team = body.get('team')


            ''' Validate team exists team name. This should not happen from UI but might happen when manually making PUT requests from POSTMan or other integrations '''
            # read data for the specific team
            teamObj = NFLTeam.getTeam(team)
            # If team is not found by team name then return error response
            if (teamObj is None):
                return {'message': f'NFL Team with name: ('+team+') not found.'}, 210


            pointsfor = body.get('pointsfor')
            pointsagainst = body.get('pointsagainst')
            playoffs = body.get('playoffs')
            gameswonaway = body.get('gameswonaway')
            gameswonathome = body.get('gameswonathome')
            gameswon = body.get('gameswon')
            gamesplayedaway = body.get('gamesplayedaway')
            gamesplayedathome = body.get('gamesplayedathome')
            gamesplayed = body.get('gamesplayed')
            gameslostaway = body.get('gameslostaway')
            gameslostathome = body.get('gameslostathome')
            gameslost = body.get('gameslost')
            gamesdrawn = body.get('gamesdrawn')
            division = body.get('division')
            id = body.get('id')
            # Create NFLTeam object
            teamObj = NFLTeam(division=division, team=team, gamesplayed=gamesplayed, gameswon=gameswon, gameslost=gameslost, gamesdrawn=gamesdrawn, gamesplayedathome=gamesplayedathome, gamesplayedaway=gamesplayedaway, gameswonathome=gameswonathome, gameslostathome=gameslostathome, gameswonaway=gameswonaway, gameslostaway=gameslostaway, gamesplayed5=0, gameswon5=0, gameslost5=0, pointsfor=pointsfor, pointsagainst=pointsagainst,  playoffs=playoffs)
           
            # update nfl team in database
            nflteam = teamObj.update(id)
            # success returns json of nfl news
            if nflteam:
                return jsonify(nflteam.read())
            # failure returns error
            return {'message': f'NFL Team not created'}, 210


    # Read NFL Team (s) Data (GET). If name request param is present, it will return
    # only that team’s data
    class _Read(Resource):
        # GET Method
        def get(self):
            # check if the team name is passed
            teamname = request.args.get("name", default="all")
            print(teamname)
           
            # if no team name is passed, read data for all teams
            if teamname == "all":
                teams = NFLTeam.query.all()    # read/extract all teams from database
                json_ready = [team.read() for team in teams]  # prepare output in json
                response = make_response(jsonify(json_ready), 200)
            else:
                # read data for the specific team
                team = NFLTeam.getTeam(teamname)
                # If team is not found by team name then return error response
                if (team is None):
                    return {'message': f'NFL Team with name: ('+teamname+') not found.'}, 210
                # return team data for the specified team
                response = make_response(jsonify(team.read()), 200)
            return response


    # Delete (Delete) method to delete a team
    # teamid (id) is required in request params
    class _Delete(Resource):
        # Delete method
        def delete(self):
            teamid = request.args.get("id")
            print(teamid)
            # Find the team with given id. Return error if team id is not provided
            # or team with given id can’t be found (this doesn’t happen from UI)
            if teamid == "":
                 return {'message': f'NFL Team ID not provided.'}, 210
            else:
                team = NFLTeam.getTeamById(teamid)


                if (team is None):
                    return {'message': f'NFL Team with ID: ('+teamid+') not found.'}, 210
               
                teamName = team._team
                print("deleting nfl team " + team._team)
                # Delete the team
                NFLTeam.delete(team)
                return {'message': f'NFL Team \''+teamName+'\' ('+teamid+') deleted.'}, 200
           


    # building RESTapi endpoint
    api.add_resource(_Create, '/create')
    api.add_resource(_Delete, '/delete')
    api.add_resource(_Update, '/update')
    api.add_resource(_Read, '/')
