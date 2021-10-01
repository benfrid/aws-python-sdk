# Use this template to create a version of the SageMaker image specified by ImageName
# Step II

# Reference link
# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_image_version

import boto3
import os

os.environ['AWS_PROFILE'] = "_____"
os.environ['AWS_DEFAULT_REGION'] = "_____"


# Set ECR as client
client = boto3.client('sagemaker')

response = client.create_image_version(
    BaseImage='___ecr_image_uri___',
    ImageName='___image_name_from_step_I___'
)

print(response)
