# Use this template to list table 

import boto3
import os

os.environ['AWS_PROFILE'] = "______"
os.environ['AWS_DEFAULT_REGION'] = "______"

client = boto3.client('athena')

response = client.list_table_metadata(
    CatalogName='______',
    DatabaseName='______'
)


for table in response['TableMetadataList']:
    print(f'  {table["Name"]}')