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

       @property
    def experience(self):
        return self._experience

    @experience.setter
    def experience(self, experience):
        self._experience = experience

    @property
    def touchdowns(self):
        return self._touchdowns

    @touchdowns.setter
    def touchdowns(self, touchdowns):
        self._touchdowns = touchdowns

    @property
    def receptions(self):
        return self._receptions

    @receptions.setter
    def receptions(self, receptions):
        self._receptions = receptions

    @property
    def passing_yards(self):
        return self._passing_yards

    @passing_yards.setter
    def passing_yards(self, passing_yards):
        self._passing_yards = passing_yards

    @property
    def rushing_yards(self):
        return self._rushing_yards

    
    @rushing_yards.setter
    def rushing_yards(self, rushing_yards):
        self._rushing_yards = rushing_yards

    @property
    def tackles(self):
        return self._tackles

    @tackles.setter
    def tackles(self, tackles):
        self._tackles = tackles

    @property
    def sacks(self):
        return self._sacks

    @sacks.setter
    def sacks(self, sacks):
        self._sacks = sacks

    @property
    def interceptions(self):
        return self._interceptions

    @interceptions.setter
    def interceptions(self, interceptions):
        self._interceptions = interceptions

   
    def __str__(self):
        return json.dumps(self.read())




    """CRUD METHODS (And More convenient methods to help out in the future) """  
    
    def create(self):
        try:
            # 
            db.session.add(self)  
            db.session.commit()  
            return self
        except IntegrityError:
            db.session.remove()
            return None


    @staticmethod
    def getPlayerById(player_id):
        return NFLPlayer.query.get(player_id)

    def update(self, player_id):
        try:
            player_to_update = NFLPlayer.getPlayerById(player_id)
            if player_to_update:
                player_to_update.name = self.name
                player_to_update.team = self.team
                player_to_update.position = self.position
                player_to_update.jersey_number = self.jersey_number
                player_to_update.age = self.age
                player_to_update.height = self.height
                player_to_update.weight = self.weight
                player_to_update.college = self.college
                player_to_update.experience = self.experience
                player_to_update.touchdowns = self.touchdowns
                player_to_update.receptions = self.receptions
                player_to_update.passing_yards = self.passing_yards
                player_to_update.rushing_yards = self.rushing_yards
                player_to_update.tackles = self.tackles
                player_to_update.sacks = self.sacks
                player_to_update.interceptions = self.interceptions

                db.session.commit()
                return NFLPlayer.getPlayerById(player_id)
            else:
                return None
        except IntegrityError:
            db.session.remove()
            return None

    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return None

    @staticmethod
    def getPlayerByName(player_name):
        return NFLPlayer.query.filter_by(name=player_name).first()

    def read(self):
        return {
            "name": self.name,
            "team": self.team,
            "position": self.position,
            "jersey_number": self.jersey_number,
            "age": self.age,
            "height": self.height,
            "weight": self.weight,
            "college": self.college,
            "experience": self.experience,
            "touchdowns": self.touchdowns,
            "receptions": self.receptions,
            "passing_yards": self.passing_yards,
            "rushing_yards": self.rushing_yards,
            "tackles": self.tackles,
            "sacks": self.sacks,
            "interceptions": self.interceptions,
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
