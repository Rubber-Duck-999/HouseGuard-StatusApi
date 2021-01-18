from flask_restful import Resource, Api, reqparse
import json
from middleware.validate import validate_alarm_event
from model.alarm_event import AlarmEventModel

parser = reqparse.RequestParser(bundle_errors=True)

class AlarmEventAPI(Resource):

    @staticmethod
    def get():

        model = AlarmEventModel()
        events = model.get_alarm_event()
        return events, 200

    @staticmethod
    def post():
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
        else:
            return 'Incomplete', 400