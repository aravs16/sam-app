import json

# import requests


def lambda_handler(event, context):
    print(event)
    print("New Feature 2")

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world, New 2",
            # "location": ip.text.replace("\n", "")
        }),
    }
