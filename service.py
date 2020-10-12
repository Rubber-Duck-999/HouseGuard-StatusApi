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
        elif "PUT" in method:
            print("Put Request")
    if 'queryStringParameters' in event and 'status' in event["queryStringParameters"]:
        # Check we have parameters
        status_message = event["queryStringParameters"]["status"]
        try:
            db = access.Access_Db(status_message)
            return status.success()
        except ValueError:
            print("Status was not provided")
            return status.failure_parameters()
        
    else:
        return status.failure_parameters()
