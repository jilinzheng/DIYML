"""
Initialize Flask, Flask-RESTful, and Redis
"""


import os
from flask import Flask
from flask_restful import Api
from rq import Queue
import rq_dashboard
from .worker import conn


# flask and flask-restful
app = Flask(__name__)
api = Api(app)

# redis and redis dashboard
REDIS = os.environ.get('REDIS', '127.0.0.1')
app.config['RQ_REDIS_URL'] = f'redis://{REDIS}:6379'#/0'
app.config["RQ_DASHBOARD_REDIS_URL"] = f'redis://{REDIS}:6379'
app.config.from_object(rq_dashboard.default_settings)
rq_dashboard.web.setup_rq_connection(app)
app.register_blueprint(rq_dashboard.blueprint, url_prefix="/rq")

# redis task queue
q = Queue(connection=conn)
