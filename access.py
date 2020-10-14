import json
import logging
import uuid

class Access_Db():

    status = "{}"
    status_type   = "latest"

    def __init__(self):
        print("Creation")

    def createStatus(self, status):
        self.status = status
        print("Creating record in db")
        print(str(self.status)
        if not dynamodb:
            dynamodb = boto3.client('dynamodb')

        table = dynamodb.Table('StatusId')
        response = table.put_item(
        Item={
                'StatusId': str(uuid.uuidv4()),
                'AlarmStatus': 'ON',
                'MemoryLeft': '0',
                'DevicesActive': '5',
                'TimeLastEscConnected': '2020',
                'LastMotionDetected': '2020',
                'LastAccessGranted': '2020',
                'LastAccessBlocked': '2020',
                'LastUser': 'Admin'
            }
        )
        return response

    def getStatus(self, status_request):
        print("Creating query for getting status record")

    