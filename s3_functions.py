import os
import logging
import boto3
from botocore.exceptions import ClientError
from KEYS import ACCESS_KEY, SECRET_ACCESS_KEY

s3_client = boto3.client(
    's3',
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_ACCESS_KEY
    )

def upload_file(file_name, bucket, object_name=None):
    if object_name is None:
        object_name = os.path.basename(file_name)

    try:
        res = s3_client.upload_file(file_name, bucket, object_name)
        if res:
            print("Successfully uploaded file")
    except ClientError as e:
        logging.error(e)
        return False
    return True

def download_file(file_name, bucket, object_name):
    try:
        res = s3_client.download_file(bucket, object_name, file_name)
        if res:
            print("Successfully downloaded file")
    except ClientError as e:
        logging.error(e)
        return False
    return True