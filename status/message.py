import json

def success():
    return {
        'statusCode': 200,
        'body': 'Success'
    }

def failure_parameters():
    return {
        'statusCode': 400,
        'body': 'Incorrect parameters'
    }

def failure_authorization():
    return {
        'statusCode': 401,
        'body': 'Authorization failure'
    }

def failure_db():
    return {
        'statusCode': 403,
        'body': 'Forbidden request'
    }