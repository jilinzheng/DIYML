"""
Main application that uses all modules.
"""
from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from auth import Users

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)


api.add_resource(Users, '/users')

if __name__ == '__main__':
    app.run(debug=True)
