# -*- coding: utf-8 -*-
import json
import access
import status
import logging

def handler(event, context):
    # Handler function
    if 'httpMethod' in event:
        method = event["httpMethod"]
        if "GET" in method:
            print("Get Request")
            return getStatus(event)
        elif "POST" in method:
            print("Post Request")
            return createStatus(event)

def getStatus(event):
    if 'queryStringParameters' in event and 'status_request' in event["queryStringParameters"]:
        # Check we have parameters
        status_request = event["queryStringParameters"]["status_request"]
        try:
            db = access.Access_Db()
            db.getStatus(status_request)
            return status.success()
        except ValueError:
            print("Status was not provided")
            return status.failure_parameters()   
    else:
        return status.failure_parameters()


def createStatus(event):
    if 'queryStringParameters' in event and 'status' in event["queryStringParameters"]:
        # Check we have parameters
        status_message = event["queryStringParameters"]["status"]
        try:
            db = access.Access_Db()
            db.createStatus(status_message)
            return status.success()
        except ValueError:
            print("Status was not provided")
            return status.failure_parameters()   
    else:
        return status.failure_parameters()

