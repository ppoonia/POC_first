import boto3

def lambda_handler(event,context):
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        filename = record['s3']['object']['key']
        print("filename {} added to the bucket {}".format(filename,bucket))

    