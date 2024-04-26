import json
import boto3

kinesis_client = boto3.client("kinesis")
stream_name = "kds-lambda-hello"
partition_key = "shardId-000000000000"


def put_record(data):
    print("begin put")
    try:
        response = kinesis_client.put_record(
            StreamName=stream_name, Data=json.dumps(data), PartitionKey=partition_key
        )
        print(response)
    except:
        print("Couldn't put data in stream ", stream_name)
        raise
    else:
        return response
