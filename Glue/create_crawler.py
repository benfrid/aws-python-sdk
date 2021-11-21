# Use this template to create a new crawler with specified targets, role, configuration, and optional schedule

# Reference link
# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.create_crawler

import boto3
import os

os.environ['AWS_PROFILE'] = "______"
os.environ['AWS_DEFAULT_REGION'] = "______"

# Set Glue as client
client = boto3.client('glue')


response = client.create_crawler(
    Name='______',
    Role='___name____',
    DatabaseName='___db_to_write_results___',
    Description='______',
    Targets={
        'S3Targets': [
            {
                'Path': '______'
            }
        ]
    },
    TablePrefix='______',
    SchemaChangePolicy={
        'UpdateBehavior': 'UPDATE_IN_DATABASE',
        'DeleteBehavior': 'DELETE_FROM_DATABASE'
    },
    RecrawlPolicy={
        'RecrawlBehavior': 'CRAWL_EVERYTHING'
    },
    Tags={
        '______': '______'
    }
)

print(response)
