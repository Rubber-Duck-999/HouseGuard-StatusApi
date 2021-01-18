import pymysql, json
from model.sql import Connection



class AlarmEventModel():

    @staticmethod
    def create_alarm_event(user, state):
        sql = "INSERT INTO `alarm_event` (`user`, `state`) VALUES (%s, %s)"
        values = (user, state)
        conn = Connection()
        conn.create(sql, values)


    @staticmethod
    def get_alarm_event():
        sql = "SELECT * FROM alarm_event ORDER BY event_id ASC LIMIT 5"
        conn = Connection()
        fail, events = conn.get(sql)
        data = ''
        if not fail:
            for event in events:
                event['created_time'] = event['created_time'].isoformat()

            data = {
                "length": len(events),
                "events": events
            }
        else:
            data = {
                "length": 0,
                "events": ''
            }
        return data