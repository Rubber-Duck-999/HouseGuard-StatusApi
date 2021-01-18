
from flask_restful import Resource, Api, reqparse
import json
from model.fault import FaultModel

parser = reqparse.RequestParser(bundle_errors=True)

class FaultAPI(Resource):

    @staticmethod
    def get():

        model = FaultModel()
        fault = model.get_fault()
        return fault, 200

    @staticmethod
    def post():
        """
        Uses the houseguard db to make a fault
        :return:
        """
        parser.add_argument('name', type=str, required=True)
        args = parser.parse_args()

        # Adding event to db
        model = FaultModel()
        model.create_fault(args['name'])
        return 'Complete', 200