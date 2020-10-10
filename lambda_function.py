import json

def lambda_handler(event, context):
    # TODO implement
    print(event)
    if 'queryStringParameters' in event:
        print(event['queryStringParameters'])
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
