# -*- coding: utf-8 -*-
import json


def handler(event, context):
    # Your code goes here!
    print(event)
    if 'queryStringParameters' in event:
        print(event['queryStringParameters'])
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
