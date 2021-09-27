# Use this template to return details about the IAM user or role whose credentials are used to call the operation


# Reference link
# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sts.html#STS.Client.get_caller_identity

import boto3
import os

os.environ['AWS_PROFILE'] = "....."
os.environ['AWS_DEFAULT_REGION'] = "....."


# Set ECR as client
client = boto3.client('sts')

response = client.get_caller_identity()

print(response)

print(f'Account = {response["Account"]}')
