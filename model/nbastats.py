'''
The below 7 lines import all of the modules necessary for the backend and backend/frontend connection. The especially important imports are the json, init, and sqlalchemy imports.
The "import json" import allows for the code in line 53, where the dump records are returned in json format, so that the python objects are readable in JSON format (text format). SQLAlchemy
is the database library being used to store all of the database info for this feature. Finally, the _init_ module is necessary, as it lets the interpreter know that there is Python code in a particular directory. 
In this case, there is Python code in the /api and /model directories.
'''

from random import randrange
from datetime import date
import os, base64
import json

from __init__ import app, db
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash, check_password_hash

'''
The below is where the "NBAStats" class is being defined. This contains all of the data for the feature that needs to be managed.
'''
class NBAStats(db.Model):
    __tablename__ = 'NBAStats'  
    
    '''
    The below sets all of the keys that are going to be looked at. The id key is special, as it is the primary key. This is what any sort of PUT and DELETE requests will be passed through if operable.
    '''
    id = db.Column(db.Integer, primary_key=True)
    _name = db.Column(db.String(255), nullable=False)
    _team = db.Column(db.String(255), nullable=False)
    _height = db.Column(db.Integer, nullable=False)
    _weight = db.Column(db.Integer, nullable=False)
    _gamesplayed = db.Column(db.Integer, nullable=False)
    _avgminutes = db.Column(db.Integer, nullable=False)
    _ppg = db.Column(db.Integer, nullable=False)
    _fgpercent = db.Column(db.Integer, nullable=False )
    _threepercent = db.Column(db.Integer, nullable=False)
    _ftpercent = db.Column(db.Integer, nullable=False)
    _orebounds = db.Column(db.Integer, nullable=False)
    _drebounds = db.Column(db.Integer, nullable=False)
    _assists = db.Column(db.Integer, nullable=False)
    _steals = db.Column(db.Integer, nullable=False) 
    _blocks = db.Column(db.Integer, nullable=False)   
    
    '''
    This is constructing the fact object and the "_init_" portion is initializing the variables within that fact object. 
    In this case, this is the fact, date, and year variables that are within this object.
    '''
    def __init__(self, name, team, height, weight, gamesplayed, avgminutes, ppg, fgpercent, threepercent, ftpercent, orebounds, drebounds, assists, steals, blocks):
        self._name = name
        self._team = team
        self._height  = height
        self._weight = weight
        self._gamesplayed = gamesplayed
        self._avgminutes = avgminutes
        self._ppg = ppg
        self._fgpercent = fgpercent
        self._threepercent = threepercent
        self._ftpercent = ftpercent
        self._orebounds = orebounds
        self._drebounds = drebounds 
        self._assists = assists
        self._steals = steals 
        self._blocks = blocks
    
    '''
    the following lines 44-75 contain the setter and getter methods. each of the three above variables (fact, date, year)
    are being extracted from the object and then updated after the object is created. 
    '''
    
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
    def gamesplayed(self):
        return self._gamesplayed
    
    @gamesplayed.setter
    def weight(self, gamesplayed):
       self._gamesplayed = gamesplayed
    
    @property
    def avgminutes(self):
        return self._avgminutes
    
    @avgminutes.setter
    def avgminutes(self, avgminutes):
       self._avgminutes = avgminutes
    
    @property
    def ppg(self):
        return self._ppg
    
    @ppg.setter
    def ppg(self, ppg):
       self._ppg = ppg
    
    @property
    def fgpercent(self):
        return self._fgpercent
    
    @fgpercent.setter
    def fgpercent(self, fgpercent):
       self._fgpercent = fgpercent 
       
    @property
    def threepercent(self):
        return self._threepercent
    
    @threepercent.setter
    def threepercent(self, threepercent):
       self._threepercent = threepercent 
    
    @property
    def ftpercent(self):
        return self._ftpercent
    
    @ftpercent.setter
    def ftpercent(self, ftpercent):
       self._ftpercent = ftpercent 
    
    @property
    def orebounds(self):
        return self._orebounds
    
    @orebounds.setter
    def orebounds(self, orebounds):
       self._orebounds = orebounds
    
    @property
    def drebounds(self):
        return self._drebounds
    
    @drebounds.setter
    def drebounds(self, drebounds):
       self._drebounds = drebounds
    
    @property
    def assists(self):
        return self._assists
    
    @assists.setter
    def assists(self, assists):
       self._assists = assists
    
    @property
    def steals(self):
        return self._steals
    
    @steals.setter
    def steals(self, steals):
       self._steals = steals
    
    @property
    def blocks(self):
        return self._blocks
    
    @blocks.setter
    def blocks(self, blocks):
       self._blocks = blocks
    
    
    
    '''
    The content is being outputted using "str(self)". It is being returned in JSON format, which is a readable format. This is a getter function.
    '''
    def __str__(self):
        return json.dumps(self.read())
    
    
    '''
    defining the create method. self allows us to access all of the attributes 
    of the current object. after the create method is defined, the data is queried from the DB.
    in this case, since it is the create method, the data is being ADDED, and then db.session.commit() is used
    to commit the DB transaction and apply the change to the DB.
    '''
    
    '''
    here, there is an integrity error "except" statement. db.session would be autocommitted 
    without the db.session.remove() line, and that's something we don't want for the purpose of the project.
    '''
    def create(self):
        try:
            db.session.add(self)  
            db.session.commit() 
            return self
        except IntegrityError:
            db.session.remove()
            return None
    
    '''
    the delete method is defined with the "self" parameter. this method is mainly for certain instances in the DB being 
    garbage collected, and the object kills itself.
    '''

    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return None
    
    '''
    read method with the self parameter, reading the object with all of the 
    properties: fact, date, and year are being returned.
    '''
    def read(self):
        return {
            "name" : self.name,
            "team" : self.team,
            "height" : self.height,
            "weight" : self.weight,
            "gamesplayed" : self.gamesplayed,
            "avgminutes" : self.avgminutes,
            "ppg" : self.ppg,
            "fgpercent" : self.fgpercent,
            "threepercent": self.threepercent,
            "ftpercent": self.ftpercent,
            "orebounds": self.orebounds,
            "drebounds": self.drebounds,
            "assists": self.assists,
            "steals": self.steals,
            "blocks": self.blocks
        }

'''
handling the situation where the table is completely empty,
returns the length from the session query of the initialized class FactofDay to be 0.
''' 
def stats_table_empty():
    return len(db.session.query(NBAStats).all()) == 0

'''
defines the initFactDay function, and then creates the tables and the DB here through the db.create_all() method.
'''
def initNBAStats():
    db.create_all()
    #db.init_app(app)
    if not stats_table_empty():
        return
    
    print("Creating data")
    """Create database and tables"""
    """Data for table"""
    
    s1 = NBAStats("Arizona became the 48th state in the Union.", "February 14th", 1912)
    s2 = NBAStats("The USS Maine Sank after an explosion in Havana Harbor", "February 15th", 1898)
    s3 = NBAStats("Power in Cuba was seized by Fidel Castro", "February 16th", 1959)

    
    '''
    the variable "statslist" being used for the tester data, containing s1, s2, 
    and s3, the variables with the sample data above.
    '''
    statslist = [s1, s2, s3]
    
    
    '''
    the below is for the sample data: for each fact in the defined factlist, the DB session will add that fact, and then commit the transaction
    with the next line. or, if there is bad/duplicate data, the data will not be committed, and session will be rolled back to its previous
    state. 
    '''

    for stat in statslist:
        try:
            db.session.add(stat)
            db.session.commit()
        except IntegrityError as e:
            print("Error: " +str(e))
            '''fails with bad or duplicate data'''
            db.session.rollback()    
