import boto3
import logging
from botocore.exceptions import ClientError
import os
BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))

bucket_name = 'shahbaz-bucket'


def download_file(file_name):
    s3 = boto3.client('s3')
    try:
        response = s3.download_file(
            bucket_name, file_name, BASE_DIR + '/downloads/' + file_name)
    except ClientError as e:
        if e.response['Error']['Code'] == '404':
            print("Item not found")
        return False
    return True


# print(download_file('my.txt'))
