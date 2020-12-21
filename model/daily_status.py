import json
from model.sql import Connection



class DailyStatusModel():

    def create_status(self, status):
            
        sql = "INSERT INTO `daily_status` (`created_date`, `allowed_devices`, `blocked_devices`, `unknown_devices`, `total_events`, `common_event`, `total_faults`, `common_fault`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        values = (status.created_date, status.allowed_devices, status.blocked_devices, status.unknown_devices, status.total_events, status.common_event, status.total_faults, status.common_fault)
        conn = Connection()
        conn.create(sql, values)

    def get_status(self):
        sql = "SELECT * FROM daily_status ORDER BY daily_status_id ASC limit 5"
        conn = Connection()
        statuses = conn.get(sql)
        for status in statuses:
            status['created_date'] = status['created_date'].isoformat()
        
        data = {
            "length": len(statuses),
            "status": statuses
        }
        return data
