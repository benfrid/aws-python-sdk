# Use this template to delete a specified development endpoint.

# Reference link
# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.delete_dev_endpoint

import boto3
import os

os.environ['AWS_PROFILE'] = "_____"
os.environ['AWS_DEFAULT_REGION'] = "_____"

# Set Glue as client
client = boto3.client('glue')

response = client.delete_dev_endpoint(
    EndpointName='_____'
)

print(response)
