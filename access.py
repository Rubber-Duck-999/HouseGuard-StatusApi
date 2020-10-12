import json
import logging

class Access_Db():

    def __init__(self, status):
        self.status = status
        if self.status is None:
            raise ValueError("Status has not been given")
        
    def putStatus(self):
        print("Creating record in db")

    def getStatus(self):
        print("Creating query for getting status record")