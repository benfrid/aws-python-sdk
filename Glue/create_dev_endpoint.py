# Use this template to create a new development endpoint

# Reference link
# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.create_dev_endpoint

import boto3
import os

os.environ['AWS_PROFILE'] = "______"
os.environ['AWS_DEFAULT_REGION'] = "______"

# Set Glue as client
client = boto3.client('glue')


response = client.create_dev_endpoint(
    EndpointName='______',
    RoleArn='______',
    PublicKeys=[
        '______',
    ],
    GlueVersion='1.0',
    NumberOfNodes=10,
    Tags={
        '__Key__': '__Value__'
    },
    Arguments={
        '--enable-glue-datacatalog': ' ',
        'GLUE_PYTHON_VERSION': '3'
    }
)

print(response)
