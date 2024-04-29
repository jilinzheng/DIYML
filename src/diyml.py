"""
Main application that combines all other modules.
"""


import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src import app, api
from src.users import UserAPI
from src.image_upload import ImageAPI
from src.training import TrainingAPI
from src.inference import InferenceAPI


@app.route('/', methods=['GET'])
def home():
    """ Temporary route for debug purposes. """
    return 'hello world!'


api.add_resource(UserAPI, '/user')
api.add_resource(ImageAPI,'/image')
api.add_resource(TrainingAPI,'/model/training')
api.add_resource(InferenceAPI,'/model/inference')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
