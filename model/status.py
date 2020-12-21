import json
from model.sql import Connection

class StatusModel():

    def create_status(self, status):   
        sql = "INSERT INTO `status` (`motion_detected`, `access_granted`, `access_denied`, `last_fault`, `last_user`, `cpu_temp`, `cpu_usage`, `memory`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        values = (status.motion, status.granted, status.denied, status.fault, status.user, status.temp, status.usage, status.memory)
        conn = Connection()
        conn.create(sql, values)

    def get_status(self):
        sql = "SELECT * FROM status ORDER BY status_id ASC limit 5"
        conn = Connection()
        statuses = conn.get(sql)
        for status in statuses:
            status['created_date']    = status['created_date'].isoformat()
            status['motion_detected'] = status['motion_detected'].isoformat()
            status['access_granted']  = status['access_granted'].isoformat()
            status['access_denied']   = status['access_denied'].isoformat()
            
        data = {
            "length": len(statuses),
            "status": statuses
        }
        return data