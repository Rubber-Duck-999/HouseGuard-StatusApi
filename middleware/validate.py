import json
import datetime
from json import JSONEncoder

def validate_alarm_event(user, state):
    valid = False
    user = user.lower().capitalize()
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

class Status():
    def __init__(self, motion, granted, denied, fault,
                user, temp, usage, memory):
        self.valid = False
        self.motion = motion
        self.granted = granted
        self.denied = denied
        self.fault = fault
        self.user = user
        self.temp = temp
        self.usage = usage
        self.memory = memory
        
class DailyStatus():
    def __init__(self, created_date, 
        allowed_devices, blocked_devices, 
        unknown_devices, total_events, common_event, 
        total_faults, common_fault):
        self.valid = False
        self.created_date = created_date
        self.allowed_devices = allowed_devices
        self.blocked_devices = blocked_devices
        self.unknown_devices = unknown_devices
        self.total_events = total_events
        self.common_event = common_event
        self.total_faults = total_faults
        self.common_fault = common_fault
        