"""
Helper json-encoding function for returning request data. 
"""

import json
from bson import json_util
def json_encode(target):
    ''' json-encoding helper function for request return data '''
    return json.loads(json_util.dumps(target))
