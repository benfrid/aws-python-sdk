# Use this template to create a custom SageMaker image
# Step I

# Reference link
# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_image

import boto3
import os

os.environ['AWS_PROFILE'] = "_____"
os.environ['AWS_DEFAULT_REGION'] = "_____"


# Set ECR as client
client = boto3.client('sagemaker')

response = client.create_image(
    Description='_____',
    DisplayName='___DisplayName___',
    ImageName='___Name___',
    RoleArn='___sagemaker_role_arn___',
    Tags=[
        {
            'Key': '_____',
            'Value': '_____'
        },
    ]
)

print(response)
