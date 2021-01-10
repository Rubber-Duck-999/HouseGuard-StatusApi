from flask_restful import Resource, Api, reqparse
import json
from model.motion import MotionModel

class MotionAPI(Resource):

    def get(self):

        model = MotionModel()
        motion = model.get_motion()
        return motion, 200

    def post(self):
        """
        Uses the houseguard db to make a motion
        :return:
        """

        # Adding event to db
        model = MotionModel()
        model.create_motion()
        return 'Complete', 200