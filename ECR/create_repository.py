# Use this template to create a repository in ECR

# Reference link
# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecr.html#ECR.Client.create_repository

import boto3
import os

os.environ['AWS_PROFILE'] = "______"
os.environ['AWS_DEFAULT_REGION'] = "______"


# Set ECR as client
client = boto3.client('ecr')


# Refer link for more detailed information. The registryId can be ignored as using it results in error(Unknown parameter in input: "registryId").
response = client.create_repository(
    repositoryName='string',
    tags=[
        {
            'Key': 'string ',
            'Value': 'string'
        },
    ],
    imageTagMutability='MUTABLE',
    imageScanningConfiguration={
        'scanOnPush': False
    },
    encryptionConfiguration={
        'encryptionType': 'AES256'
    }
)
