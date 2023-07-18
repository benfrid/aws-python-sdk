# Use this template to list databases in Athena

import boto3
import os

os.environ['AWS_PROFILE'] = "______"
os.environ['AWS_DEFAULT_REGION'] = "______"

client = boto3.client('athena')

response = client.list_databases(
    CatalogName='______'
)

print(response)

