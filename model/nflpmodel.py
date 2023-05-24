""" database dependencies to support sqliteDB examples """
from random import randrange
from datetime import date
import os, base64
import json

from __init__ import app, db
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash, check_password_hash



    """Defining Class and Variables"""  

class NFLPlayer(db.Model):
    __tablename__ = 'NFLPlayer'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=False, nullable=False)
    team = db.Column(db.String(255), unique=False, nullable=False)
    position = db.Column(db.String(255), unique=False, nullable=False)
    jersey_number = db.Column(db.Integer, unique=False, nullable=False)
    age = db.Column(db.Integer, unique=False, nullable=False)
    height = db.Column(db.String(20), unique=False, nullable=False)
    weight = db.Column(db.Float, unique=False, nullable=False)
    college = db.Column(db.String(255), unique=False, nullable=False)
    experience = db.Column(db.Integer, unique=False, nullable=False)
    touchdowns = db.Column(db.Integer, unique=False, nullable=False)
    receptions = db.Column(db.Integer, unique=False, nullable=False)
    passing_yards = db.Column(db.Integer, unique=False, nullable=False)
    rushing_yards = db.Column(db.Integer, unique=False, nullable=False)
    tackles = db.Column(db.Integer, unique=False, nullable=False)
    sacks = db.Column(db.Float, unique=False, nullable=False)
    interceptions = db.Column(db.Integer, unique=False, nullable=False)



    """Constructor"""  

   def __init__(self, name, team, position, jersey_number, age, height, weight, college, experience, touchdowns, receptions, passing_yards, rushing_yards, tackles, sacks, interceptions):
        self.name = name
        self.team = team
        self.position = position
        self.jersey_number = jersey_number
        self.age = age
        self.height = height
        self.weight = weight
        self.college = college
        self.experience = experience
        self.touchdowns = touchdowns
        self.receptions = receptions
        self.passing_yards = passing_yards
        self.rushing_yards = rushing_yards
        self.tackles = tackles
        self.sacks = sacks
        self.interceptions = interceptions



 
    """Setter and Getter Methods for all Variables"""  

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def team(self):
        return self._team

    @team.setter
    def team(self, team):
        self._team = team

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, position):
        self._position = position

    @property
    def jersey_number(self):
        return self._jersey_number

    @jersey_number.setter
    def jersey_number(self, jersey_number):
        self._jersey_number = jersey_number

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        self._height = height

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, weight):
        self._weight = weight

    @property
    def college(self):
        return self._college

    @college.setter
    def college(self, college):
        self._college = college



   



   


    def __str__(self):
        return json.dumps(self.read())




    """CRUD METHODS """  
    def create(self):
        try:
            # creates a NFL News object from NFLNews(db.Model) class, passes initializers
            db.session.add(self)  # add prepares to persist NFL News object to NFLNews table
            db.session.commit()  # SqlAlchemy "unit of work pattern" requires a manual commit
            return self
        except IntegrityError:
            db.session.remove()
            return None


    # Returns a single team by its id
    def getTeamById(teamid):
        return db.session.query(NFLTeam).filter(NFLTeam.id == teamid).first()


    # Update the team values       
    def update(self, tid):
        try:
            teamToUpdate = NFLTeam.query.filter_by(id=tid).first()
            teamToUpdate._team = self.team
            teamToUpdate._division = self._division
            teamToUpdate._gamesplayed = self._gamesplayed
            teamToUpdate._gameswon = self._gameswon
            teamToUpdate._gameslost = self._gameslost
            teamToUpdate._gamesdrawn = self._gamesdrawn
            teamToUpdate._pointsagainst = self._pointsagainst
            teamToUpdate._pointsfor = self._pointsfor
            teamToUpdate._gameslostathome = self._gameslostathome
            teamToUpdate._gameswonathome = self._gameswonathome
            teamToUpdate._gamesplayedathome = self._gamesplayedathome
            teamToUpdate._gamesplayedaway = self._gamesplayedaway
            teamToUpdate._gameswonaway = self._gameswonaway
            teamToUpdate._gameslostaway = self._gameslostaway
            teamToUpdate._playoffs = self._playoffs
            db.session.commit()  # SqlAlchemy "unit of work pattern" requires a manual commit
            print(tid)
            return NFLTeam.getTeamById(teamid = tid)
        except IntegrityError:
            db.session.remove()
            return None


   
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return None


    # Find a team by its name
    def getTeam(nflteamname):
        result = db.session.query(NFLTeam).filter(NFLTeam._team == nflteamname)
        for row in result:
            return row
 
    # Return a json string representation of team object      
    def read(self):
        return {
            "division" : self.division,
            "team" : self.team,
            "gamesplayed" : self.gamesplayed,
            "gameswon" : self.gameswon,
            "gameslost" : self.gameslost,
            "gamesdrawn" : self.gamesdrawn,
            "gamesplayedathome" : self.gamesplayedathome,
            "gamesplayedaway" : self.gamesplayedaway,
            "gameswonathome" : self.gameswonathome,
            "gameslostathome" : self.gameslostathome,
            "gameswonaway" : self.gameswonaway,
            "gameslostaway" : self.gameslostaway,
            "gamesplayed5" : self.gamesplayed5,
            "gameswon5" : self.gameswon5,
            "gameslost5" : self.gameslost5,
            "pointsfor" : self.pointsfor,
            "pointsagainst" : self.pointsagainst,
            "playoffs" : self.playoffs,
            "id": self.id
        }




""" Test data creation - Database Creation and Testing """


# Builds working data for testing


def initNFLTeams():
    print("Creating test data")
    """Create database and tables"""
    db.create_all()
    """Tester data for table"""


    #NFC East
#(self, team, gamesplayed, gameswon, gameslost, gamesdrawn, gamesplayedathome, gamesplayedaway, gameswonathome, gameslostathome,                                                             gameswonaway, gameslostaway, gamesplayed5, gameswon5, gameslost5, pointsfor, pointsagainst, pointsinfourthquarter, playoffs):


    t1 = NFLTeam(division = "NFC East", team = "Washington Commanders", gamesplayed = 17, gameswon = 8, gameslost = 8, gamesdrawn = 1, gamesplayedathome=8, gamesplayedaway=9, gameswonathome=4, gameslostathome=5, gameswonaway=4, gameslostaway=3, gamesplayed5=5, gameswon5=2, gameslost5=3, pointsfor=321, pointsagainst=343, playoffs="No")
    t2 = NFLTeam(division = "NFC East", team = "New York Giants", gamesplayed = 17, gameswon = 9, gameslost = 7, gamesdrawn = 1, gamesplayedathome=9, gamesplayedaway=8, gameswonathome=5, gameslostathome=3, gameswonaway=4, gameslostaway=4, gamesplayed5=5, gameswon5=1, gameslost5=3, pointsfor=365, pointsagainst=371, playoffs="Yes")
    t3 = NFLTeam(division = "NFC East", team = "Dallas Cowboys", gamesplayed = 17, gameswon = 12, gameslost = 5, gamesdrawn = 0, gamesplayedathome=9, gamesplayedaway=8, gameswonathome=8, gameslostathome=1, gameswonaway=4, gameslostaway=4, gamesplayed5=5, gameswon5=3, gameslost5=2, pointsfor=467, pointsagainst=342, playoffs="Yes")
    t4 = NFLTeam(division = "NFC East", team = "Philadelphia Eagles", gamesplayed = 17, gameswon = 14, gameslost = 3, gamesdrawn = 0, gamesplayedathome=9, gamesplayedaway=8, gameswonathome=7, gameslostathome=2, gameswonaway=7, gameslostaway=1, gamesplayed5=5, gameswon5=4, gameslost5=1, pointsfor=477, pointsagainst=344, playoffs="Yes")


    #NFC West
   
    t5 = NFLTeam(division = "NFC West", team = "Arizona Cardinals", gamesplayed = 17, gameswon = 4, gameslost = 13, gamesdrawn = 0, gamesplayedathome=9, gamesplayedaway=8, gameswonathome=1, gameslostathome=8, gameswonaway=3, gameslostaway=5, gamesplayed5=5, gameswon5=0, gameslost5=5, pointsfor=340, pointsagainst=449, playoffs="No")
    t6 = NFLTeam(division = "NFC West",team = "Los Angeles Rams", gamesplayed = 17, gameswon = 5, gameslost = 12, gamesdrawn = 0, gamesplayedathome=9, gamesplayedaway=8, gameswonathome=4, gameslostathome=5, gameswonaway=1, gameslostaway=7, gamesplayed5=5, gameswon5=2, gameslost5=3, pointsfor=307, pointsagainst=384, playoffs="No")
    t7 = NFLTeam(division = "NFC West",team = "Seattle Seahawks", gamesplayed = 17, gameswon = 9, gameslost = 8, gamesdrawn = 0, gamesplayedathome=9, gamesplayedaway=8, gameswonathome=5, gameslostathome=4, gameswonaway=4, gameslostaway=4, gamesplayed5=5, gameswon5=2, gameslost5=3, pointsfor=407, pointsagainst=401, playoffs="Yes")
    t8 = NFLTeam(division = "NFC West",team = "San Francisco 49ers", gamesplayed = 17, gameswon = 13, gameslost = 4, gamesdrawn = 0, gamesplayedathome=9, gamesplayedaway=8, gameswonathome=8, gameslostathome=1, gameswonaway=5, gameslostaway=3, gamesplayed5=5, gameswon5=5, gameslost5=0, pointsfor=450, pointsagainst=277, playoffs="Yes")


    # NFC North
    t9 = NFLTeam(division = "NFC North",team = "Green Bay Packers", gamesplayed = 17, gameswon = 8, gameslost = 9, gamesdrawn = 0, gamesplayedathome=9, gamesplayedaway=8, gameswonathome=5, gameslostathome=4, gameswonaway=3, gameslostaway=5, gamesplayed5=5, gameswon5=4, gameslost5=1, pointsfor=370, pointsagainst=371, playoffs="No")
    t10 = NFLTeam(division = "NFC North",team = "Chicago Bears", gamesplayed = 17, gameswon = 3, gameslost = 14, gamesdrawn = 0, gamesplayedathome=9, gamesplayedaway=8, gameswonathome=2, gameslostathome=7, gameswonaway=1, gameslostaway=7, gamesplayed5=5, gameswon5=0, gameslost5=5, pointsfor=326, pointsagainst=463, playoffs="No")
    t11 = NFLTeam(division = "NFC North",team = "Detroit Lions", gamesplayed = 17, gameswon = 9, gameslost = 8, gamesdrawn = 0, gamesplayedathome=9, gamesplayedaway=8, gameswonathome=5, gameslostathome=4, gameswonaway=4, gameslostaway=4, gamesplayed5=5, gameswon5=4, gameslost5=1, pointsfor=453, pointsagainst=427, playoffs="No")
    t12 = NFLTeam(division = "NFC North",team = "Minnesota Vikings", gamesplayed = 17, gameswon = 13, gameslost = 4, gamesdrawn = 0, gamesplayedathome=9, gamesplayedaway=8, gameswonathome=8, gameslostathome=1, gameswonaway=5, gameslostaway=3, gamesplayed5=5, gameswon5=3, gameslost5=2, pointsfor=424, pointsagainst=427, playoffs="Yes")    
   


    #NFC South
    t13 = NFLTeam(division = "NFC South",team = "New Orleans Saints", gamesplayed = 17, gameswon = 7, gameslost = 10, gamesdrawn = 0, gamesplayedathome=9, gamesplayedaway=8, gameswonathome=4, gameslostathome=5, gameswonaway=3, gameslostaway=5, gamesplayed5=5, gameswon5=3, gameslost5=2, pointsfor=330, pointsagainst=345, playoffs="No")
    t14 = NFLTeam(division = "NFC South",team = "Atlanta Falcons", gamesplayed = 17, gameswon = 7, gameslost = 10, gamesdrawn = 0, gamesplayedathome=9, gamesplayedaway=8, gameswonathome=6, gameslostathome=3, gameswonaway=1, gameslostaway=7, gamesplayed5=5, gameswon5=2, gameslost5=3, pointsfor=365, pointsagainst=386, playoffs="No")
    t15 = NFLTeam(division = "NFC South",team = "Tampa Bay Buccaneers", gamesplayed = 17, gameswon = 8, gameslost = 9, gamesdrawn = 0, gamesplayedathome=9, gamesplayedaway=8, gameswonathome=5, gameslostathome=4, gameswonaway=3, gameslostaway=5, gamesplayed5=5, gameswon5=2, gameslost5=3, pointsfor=313, pointsagainst=358, playoffs="Yes")
    t16 = NFLTeam(division = "NFC South",team = "Carolina Panthers", gamesplayed = 17, gameswon = 7, gameslost = 10, gamesdrawn = 0, gamesplayedathome=9, gamesplayedaway=8, gameswonathome=5, gameslostathome=4, gameswonaway=2, gameslostaway=6, gamesplayed5=5, gameswon5=3, gameslost5=2, pointsfor=347, pointsagainst=374, playoffs="No")


    nflteamsofficial = [t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16]
   
    #Half Completed from the AFC
    #u1 = NFLTeam(team = "Indeanappolis Colts", gamesplayed = 17, gameswon = 4, gameslost = 12, gamesdrawn = 0, gamesplayedathome=8, gamesplayedaway=9, gameswonathome=2, gameslostathome=6, gameswonaway=2, gameslostaway=6, gamesplayed5=5, gameswon5=2, gameslost5=3, pointsfor=289, pointsagainst=427, playoffs="No")
    #u2 = NFLTeam(team = "New England Patriots", gamesplayed = 17, gameswon = 8, gameslost = 9, gamesdrawn = 0, gamesplayedathome=8, gamesplayedaway=9, gameswonathome=4, gameslostathome=4, gameswonaway=4, gameslostaway=5, gamesplayed5=5, gameswon5=0, gameslost5=5, pointsfor=296, pointsagainst=316, playoffs="No")
    #u3 = NFLTeam(team = "Houston Texans", gamesplayed = 17, gameswon = 3, gameslost = 13, gamesdrawn = 1, gamesplayedathome=7, gamesplayedaway=9, gameswonathome=0, gameslostathome=7, gameswonaway=3, gameslostaway=6, gamesplayed5=5, gameswon5=0, gameslost5=5, pointsfor=340, pointsagainst=449, playoffs="No")
    #u4 = NFLTeam(team = "Kansas City Chiefs", gamesplayed = 17, gameswon = 4, gameslost = 13, gamesdrawn = 0, gamesplayedathome=9, gamesplayedaway=8, gameswonathome=4, gameslostathome=5, gameswonaway=4, gameslostaway=3, gamesplayed5=5, gameswon5=1, gameslost5=5, pointsfor=289, pointsagainst=420, pointsinfplayoffs="No")
   
    """Builds sample user/note(s) data"""
    for team in nflteamsofficial:
        try:
            team.create()
        except IntegrityError:
            '''fails with bad or duplicate data'''
            db.session.remove()
            print(f"Records exist, duplicate email, or error: {team.uid}")


#initNFLTeams()


#print(NFLTeam.getTeam("Atlanta Falcons").pointsagainst)
