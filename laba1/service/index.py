import json

def handler(event, context):
    params = event.get("queryStringParameters")
    response = { "queryStringParameters": params }

    print("response: ", response)

    return {
        "statusCode": 200,
        "body": json.dumps(response),
    }
