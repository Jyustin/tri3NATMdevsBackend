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
    This is constructing the player object and the "_init_" portion is initializing the variables within that player object. 
    In this case, this is the thirteen variables that are within this object.
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
    the following lines 44-75 contain the setter and getter methods. each of the above variables
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
    def gamesplayed(self, gamesplayed):
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
    properties.
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
returns the length from the session query of the initialized class NBAStats to be 0.
''' 
def stats_table_empty():
    return len(db.session.query(NBAStats).all()) == 0

'''
defines the initNBAStats function, and then creates the tables and the DB here through the db.create_all() method.
'''
def initNBAStats():
    with app.app_context():
        db.create_all()
        s1 = NBAStats("Kareem Abdul-Jabbar", "Los Angeles Lakers", 86, 225, 1560, 36.8, 24.6, 55.9, 0, 72.1, 2.6, 11.2, 3.6, 0.9, 2.6)
        s2 = NBAStats("Nate Archibald", "Milwaukee Bucks", 73, 150, 876, 35.8, 18.8, 47.2, 0, 81.4, 1.1, 2.3, 7.4, 1.1, 0.1)
        s3 = NBAStats("Paul Arizin", "Philadelphia Warriors", 77, 190, 713, 32.3, 22.8, 42.8, 0, 81.9, 0, 0, 2.3, 0, 0)
        s4 = NBAStats("Charles Barkley", "Phoenix Suns", 78, 250, 1073, 36.7, 22.1, 54, 20, 73.5, 4.2, 8.8, 3.9, 1.5, 0.8)
        s5 = NBAStats("Rick Barry", "Golden State Warriors", 79, 205, 794, 36.3, 24.8, 45.2, 1, 89.3, 1.8, 6.7, 4.9, 2.3, 0.4)
        s6 = NBAStats("Elgin Baylor", "Los Angeles Lakers", 78, 225, 846, 40.6, 27.4, 43.1, 0, 78.2, 0, 0, 4.3, 0, 0)
        s7 = NBAStats("Dave Bing", "Detroit Pistons", 74, 180, 901, 35.3, 20.3, 44.8, 0, 78.3, 0.7, 3, 6, 1.3, 0.2)
        s8 = NBAStats("Larry Bird", "Boston Celtics", 81, 220, 897, 39.5, 24.3, 49.6, 38.4, 88.6, 1.1, 9.8, 6.3, 1.7, 0.8)
        s9 = NBAStats("Wilt Chamberlain", "Los Angeles Lakers", 85, 275, 1045, 45.8, 30.1, 54, 0, 51.1, 4.4, 22.9, 4.4, 1, 2.4)
        s10 = NBAStats("Bob Cousy", "Boston Celtics", 73, 175, 924, 34.5, 18.4, 37.5, 0, 80.6, 0, 0, 7.5, 0, 0)
        s11 = NBAStats("Dave Cowens", "Boston Celtics", 81, 230, 766, 35.8, 17.6, 46.1, 0, 78.9, 3.8, 11.3, 3.9, 1.1, 0.9)
        s12 = NBAStats("Billy Cunningham", "Philadelphia 76ers", 79, 210, 654, 35.6, 21.2, 45.6, 0, 77.6, 2.4, 8.7, 3.7, 1.1, 0.6)
        s13 = NBAStats("Dave DeBusschere", "New York Knicks", 79, 220, 875, 38.4, 16.1, 43.4, 0, 67.9, 1.8, 9.1, 2.7, 0.9, 0.4)
        s14 = NBAStats("Clyde Drexler", "Houston Rockets", 79, 210, 1086, 34.6, 20.4, 47.2, 32.7, 78.8, 1.7, 5.6, 6.1, 2, 0.7)
        s15 = NBAStats("Julius Erving", "Philadelphia 76ers", 79, 210, 836, 34.3, 22, 50.6, 0, 77.7, 2.1, 5.2, 4.2, 1.8, 1.2)
        s16 = NBAStats("Patrick Ewing", "New York Knicks", 84, 240, 1183, 34.3, 21, 50.4, 0, 74, 3.1, 9.8, 1, 0.8, 2.4)
        s17 = NBAStats("Walt Frazier", "New York Knicks", 76, 200, 825, 38.6, 18.9, 49.2, 0, 78.8, 1.2, 4.3, 6.1, 1.9, 0.3)
        s18 = NBAStats("George Gervin", "San Antonio Spurs", 79, 180, 791, 33.8, 26.2, 51.1, 0, 84.9, 1.6, 4.6, 2.8, 1, 0.8)
        s19 = NBAStats("Hal Greer", "Philadelphia 76ers", 74, 175, 1122, 35.7, 19.2, 45.1, 0, 80.1, 0.6, 0, 4, 1, 0)
        s20 = NBAStats("John Havlicek", "Boston Celtics", 78, 203, 1270, 36.6, 20.8, 43.9, 0, 81.3, 1.2, 6.3, 4.8, 1.2, 0.3)
        s21 = NBAStats("Elvin Hayes", "Houston Rockets", 81, 235, 1303, 39.8, 21, 45.2, 0, 67.1, 4.5, 10.3, 1.8, 0.8, 2.1)
        s22 = NBAStats("Magic Johnson", "Los Angeles Lakers", 81, 215, 906, 36.7, 19.5, 52.1, 30.3, 84.8, 1.3, 6.3, 11.2, 1.9, 0.4)
        s23 = NBAStats("Sam Jones", "Boston Celtics", 75, 198, 871, 34.3, 17.7, 45.4, 0, 80.5, 0, 0, 2.5, 0, 0)
        s24 = NBAStats("Michael Jordan", "Chicago Bulls", 78, 216, 1072, 38.3, 30.1, 49.7, 32.7, 83.5, 1.6, 6.2, 5.3, 2.3, 0.8)
        s25 = NBAStats("Jerry Lucas", "Cincinnati Royals", 81, 230, 829, 33.7, 17, 49.1, 0, 80.2, 3.4, 11.9, 2.3, 0.6, 0.5)
        s26 = NBAStats("Karl Malone", "Utah Jazz", 81, 250, 1476, 37.2, 25, 51.6, 27.9, 74.2, 2.4, 9.4, 3.6, 1.4, 0.8)
        s27 = NBAStats("Moses Malone", "Philadelphia 76ers", 83, 215, 1329, 33.9, 20.6, 49.5, 0, 76.9, 3.3, 8.5, 1.4, 1.3, 1.3)
        s28 = NBAStats("Pete Maravich", "Atlanta Hawks", 76, 197, 658, 36.3, 24.2, 44.2, 0, 82, 0.4, 4, 5.4, 1.4, 0.2)
        s29 = NBAStats("Kevin McHale", "Boston Celtics", 81, 210, 971, 31.1, 17.9, 55.4, 0, 80.4, 2, 4.2, 1.7, 1, 1.7)
        s30 = NBAStats("George Mikan", "Minneapolis Lakers", 82, 245, 439, 33.8, 23.1, 40.4, 0, 78.3, 0, 0, 0, 0, 0)
        s31 = NBAStats("Earl Monroe", "New York Knicks", 75, 185, 926, 33.8, 18.8, 49.4, 0, 79.9, 0, 0, 3.9, 0, 0)
        s32 = NBAStats("Hakeem Olajuwon", "Houston Rockets", 83, 255, 1238, 35.7, 21.8, 51.2, 20.7, 71.2, 3.1, 8.5, 2.5, 1.7, 3.1)
        s33 = NBAStats("Shaquille O'Neal", "Los Angeles Lakers", 85, 325, 1207, 34.7, 23.7, 58.2, 4.5, 52.7, 2.4, 7.9, 2.5, 0.6, 2.3)
        s34 = NBAStats("Robert Parish", "Boston Celtics", 84, 230, 1611, 33.3, 14.5, 53.9, 5.9, 72.1, 3.5, 6.9, 1.4, 1.2, 1.4)
        s35 = NBAStats("Bob Pettit", "Milwaukee Hawks", 80, 220, 792, 36.8, 26.4, 43.6, 24, 76.3, 4.5, 12.2, 3, 0.7, 0.8)
        s36 = NBAStats("Scottie Pippen", "Chicago Bulls", 79, 210, 1178, 34.9, 16.1, 47.3, 32.6, 70.4, 1.9, 4.8, 5.2, 2, 0.9)
        s37 = NBAStats("Willis Reed", "New York Knicks", 81, 235, 650, 35.4, 18.7, 47.9, 0, 74.3, 2.1, 9.5, 1.8, 1, 1)
        s38 = NBAStats("Oscar Robertson", "Cincinnati Royals", 76, 205, 1040, 42.2, 25.7, 48.5, 0, 83.8, 1.3, 7.5, 9.5, 0.8, 0.1)
        s39 = NBAStats("David Robinson", "San Antonio Spurs", 85, 235, 987, 34.7, 21.1, 51.8, 25, 73.6, 2.5, 7.5, 2.5, 1.4, 3)
        s40 = NBAStats("Bill Russell", "Boston Celtics", 81, 215, 963, 42.3, 15.1, 44, 0, 56.1, 4.3, 13.9, 4.3, 1.1, 2.5)
        s41 = NBAStats("Dolph Schayes", "Syracuse Nationals", 79, 220, 996, 38.1, 18.5, 38.2, 0, 84.9, 0, 0, 3.1, 0, 0)
        s42 = NBAStats("Bill Sharman", "Boston Celtics", 73, 175, 711, 32.5, 17.8, 41.5, 0, 88.3, 0, 0, 3.9, 0, 0)
        s43 = NBAStats("John Stockton", "Utah Jazz", 73, 175, 1504, 31.8, 13.1, 51.5, 38.4, 82.6, 0.8, 2.7, 10.5, 2.2, 0.2)
        s44 = NBAStats("Isiah Thomas", "Detroit Pistons", 73, 180, 979, 35.5, 19.2, 45.2, 29.5, 75.9, 0.9, 2.8, 9.3, 1.9, 0.2)
        s45 = NBAStats("Nate Thurmond", "San Francisco Warriors", 83, 225, 964, 36.6, 15, 42.8, 0, 66.5, 4.4, 14.4, 2.7, 1, 2.2)
        s46 = NBAStats("Dwyane Wade", "Miami Heat", 76, 220, 982, 34.7, 22, 48.8, 29.7, 76.5, 1.1, 3.9, 5.4, 1.6, 0.9)
        s47 = NBAStats("Jerry West", "Los Angeles Lakers", 74, 175, 932, 39.2, 27, 47.4, 30.3, 81.4, 1.1, 3.6, 6.7, 2.6, 0.7)
        s48 = NBAStats("Lenny Wilkens", "St. Louis Hawks", 73, 180, 1077, 35.8, 16.5, 42.3, 0, 76.7, 0, 0, 6.7, 0, 0)
        s49 = NBAStats("LeBron James", "Los Angeles Lakers", 81, 250, 1421, 38, 28, 52, 29, 85, 2, 2, 7, 1, 1)
        s50 = NBAStats("Steph Curry", "Golden State Warriors", 83, 201, 1222, 29, 33, 51, 25, 88, 3, 1, 6, 2, 1)
        s51 = NBAStats("Kobe Bryant", "Los Angeles Lakers", 78, 212, 1346, 36.1, 25, 44.7, 32.9, 83.7, 1.1, 4.7, 4.7, 1.4, 0.5)
        s52 = NBAStats("Paul Pierce", "Boston Celtics", 79, 235, 1403, 36.6, 19.7, 44.7, 36.8, 80.6, 1.3, 4.7, 5.6, 1.3, 0.6)
        s53 = NBAStats("Gary Payton", "Seattle SuperSonics", 76, 180, 1335, 36.9, 16.3, 46.6, 31.3, 72.9, 1.8, 3.9, 6.7, 1.8, 0.2)
        s54 = NBAStats("Clyde Lovellette", "Minneapolis Lakers", 80, 234, 553, 33.2, 17, 44.3, 0, 72.9, 0, 0, 0, 0, 0)
        s55 = NBAStats("Bernard King", "New York Knicks", 79, 205, 874, 33.5, 22.5, 51.8, 21, 73.9, 1.3, 4.6, 5.8, 1.1, 0.3)
        s56 = NBAStats("Dominique Wilkins", "Atlanta Hawks", 79, 200, 1070, 35.6, 24.8, 46.1, 31.9, 81.5, 1.3, 3, 6.7, 1.3, 0.6)
        s57 = NBAStats("Yao Ming", "Houston Rockets", 85, 310, 486, 32.5, 19, 52.4, 19.2, 83.3, 0.3, 1.2, 9.2, 0.8, 1.9)
        s58 = NBAStats("George Yardley", "Fort Wayne Pistons", 78, 190, 789, 37.3, 19.2, 43.4, 0, 80.4, 0, 0, 6.8, 0, 0)
        s59 = NBAStats("Dikembe Mutombo", "Denver Nuggets", 82, 245, 388, 35.9, 17.8, 49.2, 0, 64.8, 0.1, 0.9, 12.3, 0.4, 3.3)
        s60 = NBAStats("Alonzo Mourning", "Charlotte Hornets", 78, 240, 1053, 33.7, 17.1, 52.6, 0, 69.9, 0.4, 1.5, 8.5, 0.9, 2.8)
        s61 = NBAStats("Jo Jo White", "Boston Celtics", 77, 190, 1188, 37.1, 17.2, 45.1, 0, 79.8, 0.7, 2, 4.9, 1, 0.2)
        s62 = NBAStats("Wes Unseld", "Baltimore/Washington Bullets", 82, 245, 812, 36.2, 10.8, 50.9, 0, 63.3, 1, 3, 14, 1.1, 0.4)
        s63 = NBAStats("Alex English", "Denver Nuggets", 82, 190, 2274, 37.3, 25.4, 50.5, 22.2, 83.8, 0.7, 2.6, 5.6, 1.3, 0.7)
        s64 = NBAStats("David Thompson", "Denver Nuggets", 82, 195, 2149, 37.4, 26, 50.7, 30.1, 75.3, 1.1, 0.9, 4.1, 0.8, 0.7)
        s65 = NBAStats("Scottie Pippen", "Chicago Bulls", 82, 210, 1746, 38.7, 16.5, 47.3, 32.6, 70.9, 1.9, 2.1, 6.4, 2, 0.9)
        s66 = NBAStats("Bob McAdoo", "Buffalo Braves", 82, 210, 2438, 38.4, 30.6, 51.2, 24.4, 77.1, 0.8, 0.7, 11.4, 1.7, 0.4)
        s67 = NBAStats("Adrian Dantley", "Utah Jazz", 82, 208, 2694, 37.5, 30.6, 54.6, 29.6, 81.8, 1.2, 0.5, 9.5, 1.6, 0.2)
        s68 = NBAStats("Artis Gilmore", "Chicago Bulls", 82, 240, 1959, 36.4, 18.6, 59.9, 0, 68.9, 1, 1.3, 14.6, 0.4, 0.5)
        s69 = NBAStats("Kevin Johnson", "Phoenix Suns", 82, 185, 2014, 36.9, 18.9, 52.5, 25.4, 81.5, 0.6, 0.3, 3.3, 2, 0.1)
        s70 = NBAStats("Mark Aguirre", "Dallas Mavericks", 82, 232, 2102, 37.9, 25.7, 49.3, 25.6, 74.5, 1.3, 0.4, 4.5, 1.3, 0.3)
        s71 = NBAStats("Tracy McGrady", "Orlando Magic", 82, 210, 2023, 39.4, 32.1, 45.7, 33.5, 75.5, 1.3, 0.8, 6.5, 4.4, 1.6)
        s72 = NBAStats("Anthony Davis", "Los Angeles Lakers", 64, 2443, 1879, 36.5, 51.3, 29.3, 84.6, 3.0, 1.3, 1.6, 2.3, 1.8)
        s73 = NBAStats("Klay Thompson", "Golden State Warriors", 79, 215, 615, 33.7, 19.7, 45.6, 42.0, 89.4, 0.9, 3.6, 2.3, 1.0, 0.9)
        s74 = NBAStats("Stephen Curry", "Golden State Warriors", 74, 185, 882, 34.9, 24.2, 47.6, 43.3, 90.7, 0.5, 4.8, 6.6, 1.7, 0.2)
        s75 = NBAStats("LeBron James", "Los Angeles Lakers", 80, 250, 1300, 39.6, 27.1, 50.4, 34.5, 73.1, 1.0, 7.4, 7.4, 1.6, 0.8)
        














        

        statslist = [s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16,s17,s18,s19,s20,s21,s22,s23,s24,s25,s26,s27,s28,s29,s30,s31,s32,s33,s34,s35,s36,s37,s38,s39,s40,s41,s42,s43,s44,s45,s46,s47,s48,s49,s50,s51,s52,s53,s54,s55,s56,s57,s58,s59,s60,s61,s62,s63,s64,s65,s66,s67,s68,s69,s70,s71,s72,s73]
        for stat in statslist:
            try:
                stat.create()
            except IntegrityError as e:
                print("Error: " +str(e))
            '''fails with bad or duplicate data'''
            db.session.rollback()    


        #db.init_app(app)
        if not stats_table_empty():
            return
    
        print("Creating data")
        """Create database and tables"""
        """Data for table"""
    

    
    '''
    the variable "statslist" being used for the tester data, containing s1, s2, 
    and s3, the variables with the sample data above.
    '''
    
    
    '''
    the below is for the sample data: for each fact in the defined statslist, the DB session will add that player and their stats, and then commit the transaction
    with the next line. or, if there is bad/duplicate data, the data will not be committed, and session will be rolled back to its previous
    state. 
    '''

    