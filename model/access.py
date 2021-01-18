import pymysql, json
from model.sql import Connection

class AccessModel():

    @staticmethod
    def create_access(granted, denied, user):
        sql = "INSERT INTO `access` (`access_granted`, `access_denied`, `last_user`) VALUES (%s, %s, %s)"
        values = (granted, denied, user)
        conn = Connection()
        conn.create(sql, values)


    @staticmethod
    def get_access():
        sql = "SELECT * FROM access ORDER BY access_id ASC LIMIT 5"
        conn = Connection()
        fail, events = conn.get(sql)
        data = ''
        if not fail:
            for event in events:
                event['created_date'] = event['created_date'].isoformat()

            data = {
                "length": len(events),
                "access": events
            }
        else:
            data = {
                "length": 0,
                "access": ''
            }
        return data