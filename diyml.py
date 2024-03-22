"""
Main application that combines all modules
"""


from flask import Flask
from flask_restful import Api
from authentication import UserAPI


# set up flask/flask-restful
app = Flask(__name__)
api = Api(app)


# add apis from other modules
#import data_upload # non flask restful
from data_upload import DataUpload

api.add_resource(UserAPI,
                 '/user/<string:user_name>',
                 '/user/<string:user_name>/<string:user_pass>')
api.add_resource(DataUpload,
                 '/data')


if __name__ == '__main__':
    app.run(debug=True)
