# Use this template to describe the domain.

# Reference link
# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.describe_domain

import boto3
import os

os.environ['AWS_PROFILE'] = "_______"
os.environ['AWS_DEFAULT_REGION'] = "______"


# Set ECR as client
client = boto3.client('sagemaker')

response = client.describe_domain(
    DomainId='_______'
)

print(response)