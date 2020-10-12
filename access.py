import json
import logging

class Access_Db():

    status = "{}"
    status_type   = "latest"

    def __init__(self):
        print("Creation")

    def createStatus(self, status):
        self.status = status
        print("Creating record in db")

    def getStatus(self, status_request):
        print("Creating query for getting status record")