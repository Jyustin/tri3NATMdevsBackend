from model.nfls import final_list
from flask import Blueprint, Flask, jsonify, request
from flask_restful import Api
import json

app = Flask(__name__)

@app.route('/nflstats', methods=['POST'])
def send_nfl():
    json_list = json.dumps(final_list)
    return json_list

if __name__ == '__main__':
    app.run()
