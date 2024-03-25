"""
Main application that combines all other modules.
"""


from src import app, api
from .users import UserAPI
from .image_upload import ImageAPI
from .training import TrainingAPI
from .inference import InferenceAPI


@app.route('/', methods=['GET'])
def home():
    """ Temporary route for debug purposes. """
    return f'hello world!'


api.add_resource(UserAPI, '/user')
api.add_resource(ImageAPI,'/image')
api.add_resource(TrainingAPI,'/model/training')
api.add_resource(InferenceAPI,'/model/inference')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
