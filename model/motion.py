import json
from model.sql import Connection
from datetime import datetime
class MotionModel():

    def create_motion(self):
        now = datetime.now()
        timestamp = datetime.timestamp(now)
            
        sql = "INSERT INTO `motion` (created_time) VALUES (%s)"
        values = (timestamp)
        conn = Connection()
        conn.create(sql, values)

    def get_motion(self):
        sql = "SELECT * FROM motion ORDER BY motion_id ASC limit 5"
        conn = Connection()
        fail, events = conn.get(sql)
        data = ''
        if not fail:
            for event in events:
                event['created_time'] = event['created_time']
            
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
