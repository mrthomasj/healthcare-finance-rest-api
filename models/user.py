from database.services.service import db
from sqlalchemy import func
from sqlalchemy.ext.automap import automap_base


class UserModel(db.Model):
    __tablename__ = 'USERS'
    
    uuid = db.Column(db.String(), primary_key=True)
    username = db.Column(db.String())
    password = db.Column(db.String())

    def __init__(self, username, password):
        if None == self.query(func.max(self.uuid)):
            
    