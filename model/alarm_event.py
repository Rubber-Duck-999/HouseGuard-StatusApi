import pymysql, json
from model.sql import Connection



class AlarmEventModel():

    def create_alarm_event(self, user, state):
        sql = "INSERT INTO `alarm_event` (`user`, `state`) VALUES (%s, %s)"
        values = (user, state)
        conn = Connection()
        conn.create(sql, values)


    def get_alarm_event(self):
        sql = "SELECT * FROM alarm_event ORDER BY event_id ASC LIMIT 5"
        conn = Connection()
        events = conn.get(sql)
        for event in events:
            event['created_time'] = event['created_time'].isoformat()

        data = {
            "length": len(events),
            "events": events
        }
        return data