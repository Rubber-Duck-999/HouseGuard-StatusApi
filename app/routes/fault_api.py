
from flask_restful import Resource, Api, reqparse
import json
from model.fault import FaultModel

parser = reqparse.RequestParser(bundle_errors=True)

class FaultAPI(Resource):

    def get(self):

        model = FaultModel()
        fault = model.get_fault()
        return fault, 200

    def post(self):
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