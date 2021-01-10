
from flask import request, app, Blueprint, Response, jsonify
from flask_restful import Resource, Api, reqparse
import json, datetime
from app.routes.alarm_event_api import AlarmEventAPI
from app.routes.access_api      import AccessAPI
from app.routes.device_api      import DeviceAPI
from app.routes.fault_api       import FaultAPI
from app.routes.hardware_api    import HardwareAPI
from app.routes.motion_api      import MotionAPI

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

api.add_resource(AlarmEventAPI, "/alarmEvent")
api.add_resource(AccessAPI, "/access")
api.add_resource(DeviceAPI, "/device")
api.add_resource(FaultAPI, "/fault")
api.add_resource(HardwareAPI, "/hardware")
api.add_resource(MotionAPI, "/motion")