import json

# import boto3


def lambda_handler(event, context):

    print(f"some logs 001 to console.")

    # print("boto3 version" + str(boto3.__version__))

    print(f"some logs 002 to console.")

    return {
        "statusCode": 200,
        "body": json.dumps(
            {
                "message": "hello world",
                # "location": ip.text.replace("\n", "")
            }
        ),
    }
