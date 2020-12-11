
from flask import request, app, Blueprint, Response, jsonify
from flask_restful import Resource, Api, reqparse
import json
from middleware.validate import validate_alarm_event
from model.alarm_event import AlarmEventModel

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

TODOS = {
    'event': {'task': 'build an API'}
}


parser = reqparse.RequestParser()

class AlarmEventAPI(Resource):

    def get(self):

        model = AlarmEventModel()
        event = model.get_alarm_event()
        response = json.dumps(event)
        return response, 200

    def post(self):
        """
        Uses the houseguard db to make a alarm event
        :return:
        """

        parser.add_argument('event', required=True, help="Event cannot be blank!")
        args = parser.parse_args()
        event = args['event']
        # Adding event to db
        model = AlarmEventModel()
        model.create_alarm_event(event)
        return 'Complete', 200


api.add_resource(AlarmEventAPI, "/alarmEvent")