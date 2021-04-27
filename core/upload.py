import boto3
import logging
from botocore.exceptions import ClientError
import os
BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))

bucket_name = 'shahbaz-bucket'


def upload_file(filename):
    s3 = boto3.client('s3')
    givenFile = os.path.join(BASE_DIR, 'encryptedFiles/' + filename)
    try:
        response = s3.upload_file(givenFile, bucket_name, filename)
    except ClientError as e:
        return logging.error(e)
    return True


# print(upload_file('kaleem.txt'))
