'''
Main application that uses all modules.
'''

from flask import Flask
from flask_restful import Api
from authentication import UserAPI


# set up flask/flask-restful
app = Flask(__name__)
api = Api(app)

# add apis from other modules
api.add_resource(UserAPI,
                 '/user/<string:user_name>',
                 '/user/<string:user_name>/<string:user_pass>')


if __name__ == '__main__':
    app.run(debug=True)
