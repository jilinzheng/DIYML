"""
Main application that combines all other modules.
"""


from flask import Flask
from flask_restful import Api
from src.authentication import UserAPI


# set up flask/flask-restful
app = Flask(__name__)
api = Api(app)


@app.route('/', methods=['GET'])
def home():
    """ Temporary route for debug purposes. """
    return 'hello world!'


# importing here in order to allow data_upload module to use flask app variable
from src.data_upload import ImageAPI # pylint: disable=wrong-import-position


# add resources to flask-restful
api.add_resource(UserAPI, '/user')
api.add_resource(ImageAPI,'/image')


if __name__ == '__main__':
    app.run(debug=True)
