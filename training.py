"""
Training module, using Roboflow API.
"""

from roboflow import Roboflow

def set_key_and_workspace(): # needs to be split into restful components
    rf = Roboflow(api_key=os.environ['ROBOFLOW_API_KEY']) # swap environ vars with post request data

    workspace = rf.workspace(os.environ["WORKSPACE_ID"])

