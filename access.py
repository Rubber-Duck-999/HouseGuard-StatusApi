import json
import logging
import uuid
import boto3
import status

class Access_Db():

    status_type   = "latest"

    def __init__(self):
        print("Creation")

    def createStatus(self, status_message):
        print("Creating record in db")
        if status_message == None:
            return status.failure_db()
        
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table('Status-db')
        print(status_message)
        print(status_message["alarmStatus"])
        response = table.put_item(
        Item={
                'StatusId': str(uuid.uuid4()),
                'AlarmStatus': status_message["alarmStatus"],
                'MemoryLeft': status_message["memoryLeft"],
                'DevicesActive': status_message["devicesActive"],
                'TimeLastEscConnected': status_message["escConnected"],
                'LastMotionDetected': status_message["motionDetected"],
                'LastAccessGranted': status_message["accessGranted"],
                'LastAccessBlocked': status_message["accessBlocked"],
                'LastUser': status_message["lastUser"]
            }
        )
        if response["ResponseMetadata"]["HTTPStatusCode"] == 200:
            return status.success()
        else:
            return status.failure_db()
            

    def getStatus(self, status_request):
        print("Creating query for getting status record")

    