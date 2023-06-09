import requests
import pandas as pd

url = "https://tank01-nfl-live-in-game-real-time-statistics-nfl.p.rapidapi.com/getNFLPlayerList"

headers = {
	"X-RapidAPI-Key": "825200d0f8msh414d353da41bfcfp1ddcfcjsnb40ef386fce9",
	"X-RapidAPI-Host": "tank01-nfl-live-in-game-real-time-statistics-nfl.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

response = (response.json())



# espnName list
espnName_list = []
for espnName in response["body"]:
    espnName_list.append(espnName['espnName'])

# espnIDFull list
espnID_list = []
for espnID in response["body"]:
    espnID_list.append(espnID['espnID'])

# teamID list
teamID_list = []
for teamID in response["body"]:
    teamID_list.append(teamID['teamID'])
    
# weight list
weight_list = []
for weight in response["body"]:
    weight_list.append(weight['weight'])
    
# pos list
pos_list = []
for pos in response["body"]:
    pos_list.append(pos['pos'])
    
# jerseyNum list
jerseyNum_list = []
for jerseyNum in response["body"]:
    jerseyNum_list.append(jerseyNum['jerseyNum'])
    
# height list
height_list = []
for height in response["body"]:
    height_list.append(height['height'])
    
# espnLink list
espnLink_list = []
for espnLink in response["body"]:
    espnLink_list.append(espnLink['espnLink'])

player_list = []

for player in response["body"]:
    player_data = {
        "espnName": player["espnName"],
        "espnID": player["espnID"],
        "teamID": player["teamID"],
        "weight": player["weight"],
        "pos": player["pos"],
        "jerseyNum": player["jerseyNum"],
        "height": player["height"],
        "espnLink": player["espnLink"]
    }
    player_list.append(player_data)