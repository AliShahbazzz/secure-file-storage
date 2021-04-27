import boto3
import logging
from botocore.exceptions import ClientError

# s3 = boto3.resource('s3')

# for bucket in s3.buckets.all():
#     print(bucket.name)

# data = open('img.jpg', 'rb')
# a = s3.Bucket('shahbaz-bucket').put_object(Key='img.jpg', Body=data)

# # Retrieve the list of existing buckets
# s3 = boto3.client('s3')
# response = s3.list_buckets()

# # Output the bucket names
# print('Existing buckets:')
# for bucket in response['Buckets']:
#     print(f'  {bucket["Name"]}')

# s3 = boto3.client('s3')
# try:
#     response = s3.upload_file('file.txt', 'shahbaz-bucket', 'file.txt')
# except ClientError as e:
#     print(logging.error(e))

# s3.download_file('BUCKET_NAME', 'OBJECT_NAME', 'FILE_NAME')
