# Use this template to return a list of all buckets owned by the authenticated sender of the request.


# Reference link
# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Client.list_buckets

import boto3
import os

os.environ['AWS_PROFILE'] = "______"
os.environ['AWS_DEFAULT_REGION'] = "______"


# Set ECR as client
client = boto3.client('s3')

response = client.list_buckets()

# Output the bucket names
print('Existing buckets:')
for bucket in response['Buckets']:
    print(f'  {bucket["Name"]}')
