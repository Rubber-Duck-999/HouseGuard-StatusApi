from status.message import failure_db
import pymysql
import os

class AlarmEventModel():


    def __init__(self):
        self.error = ""

        try:
            self.rds_host = os.environ['RDS']
            self.name = os.environ['NAME']
            self.password = os.environ['PASSWORD']
            self.db_name = os.environ['DB']
            self.port = os.environ['PORT_NUMBER']
            print("Connecting to db")

        except pymysql.MySQLError as e:
            print(e)
            self.invalid_conn = True



    def create_alarm_event(self, user, state):
        try:
            self.conn = pymysql.connect(
                host=self.rds_host,
                user=self.name,
                passwd=self.password,
                port=int(self.port),
                db=self.db_name,
                connect_timeout=5
            )
            cursor = self.conn.cursor()
            
            sql = "INSERT INTO `alarm_event` (`user`, `state`) VALUES (%s, %s)"
            insert_tuple = (user, state)
            cursor.execute(sql, insert_tuple)

            # connection is not autocommit by default. So you must commit to save
            # your changes.
            self.conn.commit()

            cursor.close()
            
        except pymysql.MySQLError as e:
            self.error = e
            print(e)
        else:
            self.conn.close()

    def get_alarm_event(self):
        try:
            self.conn = pymysql.connect(
                host=self.rds_host,
                user=self.name,
                passwd=self.password,
                port=int(self.port),
                db=self.db_name,
                connect_timeout=5
            )
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM alarm_event ORDER BY event_id DESC LIMIT 1")
            row = cursor.fetchone()
            print(row)

            # connection is not autocommit by default. So you must commit to save
            # your changes.
            self.conn.commit()

            cursor.close()
            
            return row
        except pymysql.MySQLError as e:
            self.error = e
            print(e)
            return ""
        else:
            self.conn.close()