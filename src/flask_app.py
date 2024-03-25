"""
Main application that combines all other modules.
"""


from flask import Flask
from flask_restful import Api
from rq import Queue
from rq.job import Job
from worker import conn
import rq_dashboard


# flask and flask-restful
app = Flask(__name__)
api = Api(app)


# redis and redis dashboard
app.config['RQ_REDIS_URL'] = 'redis://localhost:6379/0'
app.config["RQ_DASHBOARD_REDIS_URL"] = "redis://127.0.0.1:6379"
app.config.from_object(rq_dashboard.default_settings)
rq_dashboard.web.setup_rq_connection(app)
app.register_blueprint(rq_dashboard.blueprint, url_prefix="/rq")


# redis task queue
q = Queue(connection=conn)
