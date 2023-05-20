from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource, reqparse # used for REST API building
from datetime import datetime
# the class FactofDay, defined in the corresponding model file for the feature, is being imported for its usage in the api.
from model.nbastats import NBAStats

# this is where the blueprint class is defined and the url prefix is set, which is then registered to the app in the main.py file.
nbastats_api = Blueprint('nbastats_api', __name__, url_prefix='/api/nbastats')


# API docs https://flask-restful.readthedocs.io/en/latest/api.html
api = Api(nbastats_api)

# this is the main entry point for the app, with the class factAPI. 
class nbaAPI:
    # the _create class is being referred to for the post method, to post the objects.        
    class _Create(Resource):
        def post(self):
             ''' Read data for json body '''
             body = request.json
             
             ''' Avoid garbage in, error checking '''
            # validate name
            
            # here, this handles error checking, as the shortest fact in the world is 13 characters, so if the fact is less than that, it is deemed invalid and not added to the DB.
             stat = body.get('stat')
             if stat is None or len(stat) < 15:
                return {'message': f'Player is missing'}, 210
           
            # look for date, year variables
             name = body.get('name')
             team = body.get('team')
             height = body.get('height')
             weight = body.get('weight')
             gamesplayed = body.get('gamesplayed')
             avgminutes = body.get('avgminutes')
             ppg = body.get('ppg')
             fgpercent = body.get('fgpercent')
             threepercent = body.get('threepercent')
             ftpercent = body.get('ftpercent')
             orebounds = body.get('orebounds')
             drebounds = body.get('drebounds')
             assists = body.get('assists')
             steals = body.get('steals')
             blocks = body.get('blocks')


             # this sets up the fact object
             uo = NBAStats(stat, name, team, height, weight, gamesplayed, avgminutes, ppg, fgpercent, threepercent, ftpercent, orebounds, drebounds, assists, steals, blocks)
           
           
             # this adds the fact to the DB (uo.create())
             stat = uo.create()
             
             # if the addition was successful, then the fact is returned to the user in a readable JSON format.
             if stat:
                return jsonify(stat.read())
            # failure returns error
             return {'message': f'Processed fact error'}, 210
    
    # _Read class, needed for the GET request.     
    class _Read(Resource):
        def get(self):
            stats = NBAStats.query.all()    # read/extract all facts from database
            json_ready = [stat.read() for stat in stats]  # prepares the readable output in json
            return jsonify(json_ready)  # jsonify creates Flask response object, more specific to APIs than json.dumps
        


    # building the API endpoints. there is a create and read endpoint, to serve for both the GET and POST requests.
    api.add_resource(_Create, '/create')
    api.add_resource(_Read, '/')
