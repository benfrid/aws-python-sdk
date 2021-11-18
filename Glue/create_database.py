# Use this template to create a new database in glue

# Note: To grant permissions to a database, use LakeFormation

# Reference link
# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.create_database

import boto3
import os

os.environ['AWS_PROFILE'] = "______"
os.environ['AWS_DEFAULT_REGION'] = "______"

# Set Glue as client
client = boto3.client('glue')

response = client.create_database(
    DatabaseInput={
        'Name': '______',
        'Description': '______',
        'LocationUri': '___s3_bucket_location___'
    }
)

print(response)
