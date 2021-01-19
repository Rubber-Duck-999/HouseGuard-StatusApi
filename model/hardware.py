import pymysql, json
from model.sql import Connection

class HardwareModel():

    def create_hardware(self, temp, usage, memory):
        sql = "INSERT INTO `hardware` (`cpu_temp`, `cpu_usage`, `memory`) VALUES (%s, %s, %s)"
        values = (temp, usage, memory)
        conn = Connection()
        conn.create(sql, values)


    def get_hardware(self):
        sql = "SELECT * FROM hardware ORDER BY hardware_id ASC LIMIT 1"
        conn = Connection()
        fail, events = conn.get(sql)
        data = ''
        if not fail:
            for event in events:
                event['created_time'] = event['created_time'].isoformat()

            data = {
                "length": len(events),
                "hardware": events
            }
        else:
            data = {
                "length": 0,
                "hardware": ''
            }
        return data