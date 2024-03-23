"""
Main application that combines all other modules.
"""


from flask import Flask
from flask_restful import Api
from authentication import UserAPI


# set up flask/flask-restful
app = Flask(__name__)
api = Api(app)


@app.route('/', methods=['GET'])
def home():
    """ Temporary route for debug purposes. """
    return 'hello world!'


# importing here in order to allow data_upload module to use flask app variable
from data_upload import ImageUpload # pylint: disable=wrong-import-position


# add resources to flask-restful
api.add_resource(UserAPI,
                 '/user/<string:user_name>',
                 '/user/<string:user_name>/<string:user_pass>')
api.add_resource(ImageUpload,
                 '/image/<string:image_name>/<string:user_name>')


if __name__ == '__main__':
    app.run(debug=True)
