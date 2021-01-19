import pymysql, json
from model.sql import Connection

class DeviceModel():

    def create_device(self, allowed, blocked, unknown):
        sql = "INSERT INTO `device` (`allowed_devices`, `blocked_devices`, `unknown_devices`) VALUES (%s, %s, %s)"
        values = (allowed, blocked, unknown)
        conn = Connection()
        conn.create(sql, values)


    def get_device(self):
        sql = "SELECT * FROM device ORDER BY device_id ASC LIMIT 1"
        conn = Connection()
        fail, events = conn.get(sql)
        data = ''
        if not fail:
            for event in events:
                event['created_date'] = event['created_date'].isoformat()

            data = {
                "length": len(events),
                "device": events
            }
        else:
            data = {
                "length": 0,
                "device": ''
            }
        return data