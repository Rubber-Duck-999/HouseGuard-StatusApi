from flask_restful import Resource, Api, reqparse
import json
from model.device import DeviceModel

parser = reqparse.RequestParser(bundle_errors=True)

class DeviceAPI(Resource):

    @staticmethod
    def get():

        model = DeviceModel()
        device = model.get_device()
        return device, 200

    @staticmethod
    def post():
        """
        Uses the houseguard db to make a device
        :return:
        """
        parser.add_argument('allowed', type=int, required=True)
        parser.add_argument('blocked', type=int, required=True)
        parser.add_argument('unknown', type=int, required=True)
        args = parser.parse_args()

        # Adding device to db
        model = DeviceModel()
        model.create_device(args['allowed'],
                        args['blocked'],
                        args['unknown'])
        return 'Complete', 200