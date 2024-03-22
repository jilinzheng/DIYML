from roboflow import Roboflow
import os

def set_key_and_workspace():
rf = Roboflow(api_key=os.environ['ROBOFLOW_API_KEY'])

workspace = rf.workspace(os.environ["WORKSPACE_ID"])

