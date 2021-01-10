import pymysql, json
from model.sql import Connection

class DeviceModel():

    def create_device(self, allowed, blocked, unknown):
        sql = "INSERT INTO `device` (`allowed`, `blocked`, `unknown`) VALUES (%s, %s, %s)"
        values = (device.allowed, device.blocked, device.unknown)
        conn = Connection()
        conn.create(sql, values)


    def get_device(self):
        sql = "SELECT * FROM device ORDER BY device_id ASC LIMIT 5"
        conn = Connection()
        fail, events = conn.get(sql)
        data = ''
        if not fail:
            for event in events:
                event['created_time'] = event['created_time'].isoformat()

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