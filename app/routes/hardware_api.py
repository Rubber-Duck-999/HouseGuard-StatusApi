from flask_restful import Resource, Api, reqparse
import json
from model.hardware import HardwareModel

parser = reqparse.RequestParser(bundle_errors=True)

class HardwareAPI(Resource):

    @staticmethod
    def get():

        model = HardwareModel()
        hardware = model.get_hardware()
        return hardware, 200

    @staticmethod
    def post():
        """
        Uses the houseguard db to make a hardware
        :return:
        """
        parser.add_argument('cpu_temp', type=int, required=True)
        parser.add_argument('cpu_usage', type=int, required=True)
        parser.add_argument('memory', type=int, required=True)
        args = parser.parse_args()

        # Adding hardware to db
        model = HardwareModel()
        model.create_hardware(args['cpu_temp'],
                            args['cpu_usage'],
                            args['memory'])
        return 'Complete', 200