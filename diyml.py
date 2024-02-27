"""
Main application that uses all modules.
"""
import os
from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
# from auth import Users

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class Users(db.Model):
    ''' Table to hold users, '''
    uid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(200), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)

    def __init__(self, uid, username, password):
        self.uid = uid
        self.username = username
        self.password = password

    def __repr__(self):
        return self.username

#api.add_resource(Users, '/users')

if __name__ == '__main__':
    app.run(debug=True)
