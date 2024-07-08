import json

def handler(event, context):
    response = {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Hello from basic_function!",
            "event": event
        })
    }

    return response
