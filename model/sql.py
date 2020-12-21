import pymysql, os, sys

class Connection():

    def __init__(self):
        try:
            self.rds_host = os.environ['RDS']
            self.name = os.environ['NAME']
            self.password = os.environ['PASSWORD']
            self.db_name = os.environ['DB']
            self.port = os.environ['PORT_NUMBER']

        except pymysql.MySQLError as e:
            print(e)

    def create(self, sql, values):
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
            
            cursor.execute(sql, values)

            # connection is not autocommit by default. So you must commit to save
            # your changes.
            self.conn.commit()

            cursor.close()
            
        except pymysql.MySQLError as e:
            self.error = e
            print(e)
        except:
            print("Unexpected error:", sys.exc_info()[0])
        else:
            self.conn.close()
    
    def get(self, sql, values = None):
        try:
            self.conn = pymysql.connect(
                host=self.rds_host,
                user=self.name,
                passwd=self.password,
                port=int(self.port),
                db=self.db_name,
                connect_timeout=5,
                cursorclass=pymysql.cursors.DictCursor
            )
            cursor = self.conn.cursor()
            if values != None:
                cursor.execute(sql, values)
            else:
                cursor.execute(sql)
            columns=[x[0] for x in cursor.description]
            data = cursor.fetchall()

            # connection is not autocommit by default. So you must commit to save
            # your changes.
            self.conn.commit()

            cursor.close()
            return data
        except pymysql.MySQLError as e:
            self.error = e
            print(e)
        except:
            print("Unexpected error:", sys.exc_info()[0])
        else:
            self.conn.close()