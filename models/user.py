import sqlite3

from db import db



class userModel(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))

    def __init__(self,username, password):
        
        self.username = username
        self.password = password

    @classmethod #this means that we are replacing 'User' with the current class name which is also User
    def find_by_username(cls,username): #get user based on the username
        return cls.query.filter_by(username=username).first()
        
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()


    @classmethod #this means that we are replacing 'User' with the current class name which is also User
    def find_by_id(cls,_id): #get user based on the user name
         
        return cls.query.filter_by(id=_id).first()




    ##find_by_username and find_by_id are in a sense apis too, but not Rest apis because they interface the software to the database