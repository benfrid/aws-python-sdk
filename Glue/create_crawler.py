# Use this template to create a new crawler with specified targets, role, configuration, and optional schedule

# Reference link
# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.create_crawler

import boto3
import os

os.environ['AWS_PROFILE'] = "....."
os.environ['AWS_DEFAULT_REGION'] = "....."

# Set Glue as client
client = boto3.client('glue')


response = client.create_crawler(
    Name='.....',
    Role='.....',
    DatabaseName='.....',
    Description='......',
    Targets={
        'S3Targets': [
            {
                'Path': '.....'
            }
        ]
    },
    TablePrefix='.....',
    SchemaChangePolicy={
        'UpdateBehavior': 'UPDATE_IN_DATABASE',
        'DeleteBehavior': 'DELETE_FROM_DATABASE'
    },
    RecrawlPolicy={
        'RecrawlBehavior': 'CRAWL_EVERYTHING'
    },
    Tags={
        'created-by': '.....'
    }
)

print(response)
