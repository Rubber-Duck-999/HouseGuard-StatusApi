import json
import datetime
from json import JSONEncoder

def validate_alarm_event(user, state):
    valid = False
    user = user.lower().capitalize()
    state = state.upper()
    if state is "ON" or "OFF":
        valid = True
    names = ['Admin', 'User']
    if any(user in s for s in names):
        valid = True
    return valid, user, state

# subclass JSONEncoder
class DateTimeEncoder(JSONEncoder):
        #Override the default method
        def default(self, obj):
            if isinstance(obj, (datetime.date, datetime.datetime)):
                return obj.isoformat()