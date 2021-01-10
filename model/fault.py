import pymysql, json
from model.sql import Connection

class FaultModel():

    def create_fault(self, name):
        sql = "INSERT INTO `fault` (`name`) VALUES (%s)"
        values = (name)
        conn = Connection()
        conn.create(sql, values)


    def get_fault(self):
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