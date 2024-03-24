"""
Main application that combines all other modules.
"""


from flask import Flask
from flask_restful import Api
from src.users import UserAPI
from src.image_upload import ImageAPI
from src.training import TrainingAPI
from src.inference import InferenceAPI


# set up flask/flask-restful
app = Flask(__name__)
api = Api(app)


@app.route('/', methods=['GET'])
def home():
    """ Temporary route for debug purposes. """
    return 'hello world!'


# add resources to flask-restful
api.add_resource(UserAPI, '/user')
api.add_resource(ImageAPI,'/image')
api.add_resource(TrainingAPI,'/model/training')
api.add_resource(InferenceAPI,'/model/inference')


if __name__ == '__main__':
    app.run(debug=True)
