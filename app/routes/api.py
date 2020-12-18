
from flask import request, app, Blueprint, Response, jsonify
from flask_restful import Resource, Api, reqparse
import json
from middleware.validate import validate_alarm_event, DateTimeEncoder
from model.alarm_event import AlarmEventModel
import datetime

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

TODOS = {
    'event': {'task': 'build an API'}
}


parser = reqparse.RequestParser()

def datetime_handler(x):
    if isinstance(x, datetime.datetime):
        return x.isoformat()
    raise TypeError("Unknown type")

class AlarmEventAPI(Resource):

    def get(self):

        model = AlarmEventModel()
        events = model.get_alarm_event()
        return json.dumps(events, cls=DateTimeEncoder)

    def post(self):
        """
        Uses the houseguard db to make a alarm event
        :return:
        """
        parser.add_argument('user', type=str)
        parser.add_argument('state', type=str)
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

        model = AlarmEventModel()
        event = model.get_alarm_event()
        response = json.dumps(event, cls=DateTimeEncoder)
        return response, 200

    def post(self):
        """
        Uses the houseguard db to make a alarm event
        :return:
        """
        parser.add_argument('user', type=str)
        parser.add_argument('state', type=str)
        args = parser.parse_args()

        # Adding event to db
        model = AlarmEventModel()
        user = args['user']
        state = args['state']
        valid, user, state = validate_alarm_event(user, state)
        if valid:
            model.create_alarm_event(user, state)
        return 'Complete', 200


api.add_resource(AlarmEventAPI, "/alarmEvent")
api.add_resource(StatusAPI, "/status")