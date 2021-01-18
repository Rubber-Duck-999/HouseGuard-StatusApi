
from flask_restful import Resource, Api, reqparse
import json
from model.access import AccessModel

parser = reqparse.RequestParser(bundle_errors=True)

class AccessAPI(Resource):

    @staticmethod
    def get():

        model = AccessModel()
        access = model.get_access()
        return access, 200

    @staticmethod
    def post():
        """
        Uses the houseguard db to make a access
        :return:
        """
        parser.add_argument('access_granted', type=str, required=True)
        parser.add_argument('access_denied', type=str, required=True)
        parser.add_argument('last_user', type=str, required=True)
        args = parser.parse_args()

        # Adding event to db
        model = AccessModel()
        model.create_access(args['access_granted'], 
                        args['access_denied'], 
                        args['last_user'])
        return 'Complete', 200