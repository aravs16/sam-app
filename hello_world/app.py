import json

# import requests


def lambda_handler(event, context):
    print(event)
    print("New Feature prod")

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world, New",
            # "location": ip.text.replace("\n", "")
        }),
    }
