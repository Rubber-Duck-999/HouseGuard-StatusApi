import pymysql, json
from model.sql import Connection

class FaultModel():

    @staticmethod
    def create_fault(name):
        sql = "INSERT INTO `fault` (`name`) VALUES (%s)"
        values = (name)
        conn = Connection()
        conn.create(sql, values)


    @staticmethod
    def get_fault():
        sql = "SELECT * FROM fault ORDER BY fault_id ASC LIMIT 5"
        conn = Connection()
        fail, events = conn.get(sql)
        data = ''
        if not fail:
            for event in events:
                event['created_time'] = event['created_time'].isoformat()

            data = {
                "length": len(events),
                "fault": events
            }
        else:
            data = {
                "length": 0,
                "fault": ''
            }
        return data