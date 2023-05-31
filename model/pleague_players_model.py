""" database dependencies to support sqliteDB examples """
from random import randrange
from datetime import date
import os, base64
import json

from __init__ import app, db
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash, check_password_hash

# ensure that JSON sorting doesn't change the order of values in view
app.config['JSON_SORT_KEYS'] = False

"""Premier League Player class"""
class PremierLeaguePlayer(db.Model):
    __tablename__ = 'PremierLeaguePlayer'

    id = db.Column(db.Integer, primary_key=True)
    _name = db.Column(db.String(255), unique=False, nullable=False)
    _team = db.Column(db.String(255), unique=False, nullable=False)
    _position = db.Column(db.String(255), unique=False, nullable=False)
    _jersey_number = db.Column(db.Integer, unique=False, nullable=False)
    _age = db.Column(db.Integer, unique=False, nullable=False)
    _height = db.Column(db.String(20), unique=False, nullable=False)
    _weight = db.Column(db.Float, unique=False, nullable=False)
    _goals = db.Column(db.Integer, unique=False, nullable=False)
    _assists = db.Column(db.Integer, unique=False, nullable=False)
    _yellow_cards = db.Column(db.Integer, unique=False, nullable=False)
    _red_cards = db.Column(db.Integer, unique=False, nullable=False)
    _passes_completed = db.Column(db.Integer, unique=False, nullable=False)
    _tackles = db.Column(db.Integer, unique=False, nullable=False)
    _clean_sheets = db.Column(db.Integer, unique=False, nullable=False)

    """Constructor"""

    def __init__(self, name, team, position, jersey_number, age, height, weight, goals, assists, yellow_cards, red_cards, passes_completed, tackles, clean_sheets):
        self.name = name
        self.team = team
        self.position = position
        self.jersey_number = jersey_number
        self.age = age
        self.height = height
        self.weight = weight
        self.goals = goals
        self.assists = assists
        self.yellow_cards = yellow_cards
        self.red_cards = red_cards
        self.passes_completed = passes_completed
        self.tackles = tackles
        self.clean_sheets = clean_sheets



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
    def goals(self):
        return self._goals

    @goals.setter
    def goals(self, goals):
        self._goals = goals

    @property
    def assists(self):
        return self._assists

    @assists.setter
    def assists(self, assists):
        self._assists = assists

    @property
    def yellow_cards(self):
        return self._yellow_cards

    @yellow_cards.setter
    def yellow_cards(self, yellow_cards):
        self._yellow_cards = yellow_cards

    @property
    def red_cards(self):
        return self._red_cards

    @red_cards.setter
    def red_cards(self, red_cards):
        self._red_cards = red_cards

    @property
    def passes_completed(self):
        return self._passes_completed

    @passes_completed.setter
    def passes_completed(self, passes_completed):
        self._passes_completed = passes_completed

    @property
    def tackles(self):
        return self._tackles

    @tackles.setter
    def tackles(self, tackles):
        self._tackles = tackles

    @property
    def clean_sheets(self):
        return self._clean_sheets

    @clean_sheets.setter
    def clean_sheets(self, clean_sheets):
        self._clean_sheets = clean_sheets
        


    """CRUD METHODS (And More convenient methods to help out in the future)"""

    def create(self):
        try:
            db.session.add(self)
            db.session.commit()
            return self
        except IntegrityError:
            db.session.remove()
            return None

    @staticmethod
    def getPlayerById(player_id):
        return PremierLeaguePlayer.query.get(player_id)

    def update(self, player_id):
        try:
            player_to_update = PremierLeaguePlayer.getPlayerById(player_id)
            if player_to_update:
                player_to_update.name = self.name
                player_to_update.team = self.team
                player_to_update.position = self.position
                player_to_update.jersey_number = self.jersey_number
                player_to_update.age = self.age
                player_to_update.height = self.height
                player_to_update.weight = self.weight
                player_to_update.goals = self.goals
                player_to_update.assists = self.assists
                player_to_update.yellow_cards = self.yellow_cards
                player_to_update.red_cards = self.red_cards
                player_to_update.passes_completed = self.passes_completed
                player_to_update.tackles = self.tackles
                player_to_update.clean_sheets = self.clean_sheets

                db.session.commit()
                return player_to_update
            else:
                return None
        except IntegrityError:
            db.session.remove()
            return None

    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
            return True
        except:
            db.session.remove()
            return False

    @staticmethod
    def getAllPlayers():
        return PremierLeaguePlayer.query.all()
    
    '''
    read method with the self parameter, reading the object with all of the 
    properties.
    '''
    def read(self):
        return {
            "name" : self.name,
            "team" : self.team,
            "position" : self.position,
            "jersey_number" : self.jersey_number,
            "age" : self.age,
            "height" : self.height,
            "weight" : self.weight,
            "goals" : self.goals,
            "assists": self.assists,
            "yellow_cards": self.yellow_cards,
            "red_cards": self.red_cards,
            "passes_completed": self.passes_completed,
            "tackles": self.tackles,
            "clean_sheets": self.clean_sheets
        }

def initPremierLeaguePlayers():
    with app.app_context():
        print("Creating test data")
        """Create database and tables"""
        db.create_all()
        
        """Test data for table"""
        
        p1 = PremierLeaguePlayer(name="Mohamed Salah", team="Liverpool", position="Forward", jersey_number=11, age=29, height="5.7", weight=148, goals=100, assists=10, yellow_cards=0, red_cards=0, passes_completed=250, tackles=10, clean_sheets=100)
        p2 = PremierLeaguePlayer(name="Harry Kane", team="Tottenham Hotspur", position="Forward", jersey_number=10, age=28, height="5.7", weight=148, goals=100, assists=10, yellow_cards=0, red_cards=0, passes_completed=250, tackles=10, clean_sheets=100)
        p3 = PremierLeaguePlayer(name="Kevin De Bruyne", team="Manchester City", position="Midfielder", jersey_number=17, age=30, height="5.7", weight=148, goals=100, assists=10, yellow_cards=0, red_cards=0, passes_completed=250, tackles=10, clean_sheets=100)
        p4 = PremierLeaguePlayer(name="Virgil van Dijk", team="Liverpool", position="Defender", jersey_number=4, age=30, height="5.7", weight=148, goals=100, assists=10, yellow_cards=0, red_cards=0, passes_completed=250, tackles=10, clean_sheets=100)
        p5 = PremierLeaguePlayer(name="Bruno Fernandes", team="Manchester United", position="Midfielder", jersey_number=18, age=27, height="5.7", weight=148, goals=100, assists=10, yellow_cards=0, red_cards=0, passes_completed=250, tackles=10, clean_sheets=100)
        p6 = PremierLeaguePlayer(name="Jack Grealish", team="Aston Villa", position="Midfielder", jersey_number=10, age=25, height="5.7", weight=148, goals=100, assists=10, yellow_cards=0, red_cards=0, passes_completed=250, tackles=10, clean_sheets=100)
        p7 = PremierLeaguePlayer(name="Riyad Mahrez", team="Manchester City", position="Forward", jersey_number=26, age=30, height="5.7", weight=148, goals=100, assists=10, yellow_cards=0, red_cards=0, passes_completed=250, tackles=10, clean_sheets=100)
        p8 = PremierLeaguePlayer(name="N'Golo Kanté", team="Chelsea", position="Midfielder", jersey_number=7, age=30, height="5.7", weight=148, goals=100, assists=10, yellow_cards=0, red_cards=0, passes_completed=250, tackles=10, clean_sheets=100)
            
        premierleagueplayersofficial = [p1, p2, p3, p4, p5, p6, p7, p8]
            
        """Builds sample player data"""
        for player in premierleagueplayersofficial:
            try:
                player.create()
            except IntegrityError:
                db.session.remove()
                print(f"Records exist or error: {player.id}")

initPremierLeaguePlayers()
