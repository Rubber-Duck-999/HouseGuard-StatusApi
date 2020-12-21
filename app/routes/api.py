
from flask import request, app, Blueprint, Response, jsonify
from flask_restful import Resource, Api, reqparse
import json
from middleware.validate import validate_alarm_event, DateTimeEncoder, Status, DailyStatus
from model.alarm_event import AlarmEventModel
from model.status import StatusModel
from model.daily_status import DailyStatusModel
import datetime

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

TODOS = {
    'event': {'task': 'build an API'}
}


parser = reqparse.RequestParser(bundle_errors=True)

class AlarmEventAPI(Resource):

    def get(self):

        model = AlarmEventModel()
        events = model.get_alarm_event()
        return events, 200

    def post(self):
        """
        Uses the houseguard db to make a alarm event
        :return:
        """
        parser.add_argument('user', type=str, required=True)
        parser.add_argument('state', choices=['ON', 'OFF'], required=True)
        args = parser.parse_args()
    
        # Adding event to db
        model = AlarmEventModel()
        user = args['user']
        state = args['state']
        valid, user, state = validate_alarm_event(user, state)
        if valid:
            model.create_alarm_event(user, state)
        return 'Complete', 200

class StatusAPI(Resource):

    def get(self):

        model = StatusModel()
        status = model.get_status()
        return status, 200

    def post(self):
        """
        Uses the houseguard db to make a status
        :return:
        """
        parser.add_argument('motion_detected', type=str, required=True)
        parser.add_argument('access_granted', type=str, required=True)
        parser.add_argument('access_denied', type=str, required=True)
        parser.add_argument('last_fault', type=str, required=True)
        parser.add_argument('last_user', type=str, required=True)
        parser.add_argument('cpu_temp', type=int, required=True)
        parser.add_argument('cpu_usage', type=int, required=True)
        parser.add_argument('memory', type=int, required=True)
        args = parser.parse_args()

        # Adding event to db
        status = Status(args['motion_detected'], 
        args['access_granted'], args['access_denied'], 
        args['last_fault'], args['last_user'], args['cpu_temp'], 
        args['cpu_usage'], args['memory'] )
        model = StatusModel()
        model.create_status(status)
        return 'Complete', 200

class DailyStatusAPI(Resource):

    def get(self):

        model = DailyStatusModel()
        status = model.get_status()
        return status, 200

    def post(self):
        """
        Uses the houseguard db to make a daily status
        :return:
        """
        parser.add_argument('created_date', type=str, required=True)
        parser.add_argument('allowed_devices', type=int, required=True)
        parser.add_argument('blocked_devices', type=int, required=True)
        parser.add_argument('unknown_devices', type=int, required=True)
        parser.add_argument('total_events', type=int, required=True)
        parser.add_argument('common_event', type=str, required=True)
        parser.add_argument('total_faults', type=int, required=True)
        parser.add_argument('common_fault', type=str, required=True)
        args = parser.parse_args()

        # Adding event to db
        status = DailyStatus(args['created_date'], 
        args['allowed_devices'], args['blocked_devices'], 
        args['unknown_devices'], args['total_events'], args['common_event'], 
        args['total_faults'], args['common_fault'])
        model = DailyStatusModel()
        model.create_status(status)
        return 'Complete', 200

api.add_resource(AlarmEventAPI, "/alarmEvent")
api.add_resource(StatusAPI, "/status")
api.add_resource(DailyStatusAPI, "/dailyStatus")