# Use this template to create a new crawler with specified targets, role, configuration, and optional schedule

# Reference link
# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.delete_crawler

import boto3
import os

os.environ['AWS_PROFILE'] = "______"
os.environ['AWS_DEFAULT_REGION'] = "______"

# Set Glue as client
client = boto3.client('glue')

response = client.delete_crawler(
    Name='______'
)

print(response)
