import json
from model.sql import Connection
from datetime import datetime
class MotionModel():

    @staticmethod
    def create_motion():
        now = datetime.now()
        timestamp = datetime.timestamp(now)
            
        sql = "INSERT INTO `motion` (created_time) VALUES (%s)"
        values = (timestamp)
        conn = Connection()
        conn.create(sql, values)

    @staticmethod
    def get_motion():
        sql = "SELECT * FROM motion ORDER BY motion_id ASC limit 5"
        conn = Connection()
        fail, events = conn.get(sql)
        data = ''
        if not fail:
            for event in events:
                event['created_time'] = event['created_time'].isoformat()
            
            data = {
                "length": len(events),
                "motion": events
            }
        else:
            data = {
                "length": 0,
                "motion": ''
            }
        return data
