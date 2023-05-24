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

def initNFLPlayers():
    print("Creating test data")
    """Create database and tables"""
    db.create_all()
    
    """Tester data for table"""
    
    p1 = NFLPlayer(name="Tom Brady", team="Tampa Bay Buccaneers", position="Quarterback", jersey_number=12, age=44)
    p2 = NFLPlayer(name="Patrick Mahomes", team="Kansas City Chiefs", position="Quarterback", jersey_number=15, age=25)
    p3 = NFLPlayer(name="Aaron Rodgers", team="Green Bay Packers", position="Quarterback", jersey_number=12, age=37)
    p4 = NFLPlayer(name="Derrick Henry", team="Tennessee Titans", position="Running Back", jersey_number=22, age=27)
    p5 = NFLPlayer(name="Stefon Diggs", team="Buffalo Bills", position="Wide Receiver", jersey_number=14, age=27)
    p6 = NFLPlayer(name="Travis Kelce", team="Kansas City Chiefs", position="Tight End", jersey_number=87, age=32)
    p7 = NFLPlayer(name="Aaron Donald", team="Los Angeles Rams", position="Defensive Tackle", jersey_number=99, age=30)
    p8 = NFLPlayer(name="Jalen Ramsey", team="Los Angeles Rams", position="Cornerback", jersey_number=20, age=26)
    
    nflplayersofficial = [p1, p2, p3, p4, p5, p6, p7, p8]
    
    """Builds sample player data"""
    for player in nflplayersofficial:
        try:
            player.create()
        except IntegrityError:
            db.session.remove()
            print(f"Records exist or error: {player.id}")

  