# Use this template to delete an AppImageConfig.

# Reference link
# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.delete_app_image_config

import boto3
import os

os.environ['AWS_PROFILE'] = "_____"
os.environ['AWS_DEFAULT_REGION'] = "_____"


# Set ECR as client
client = boto3.client('sagemaker')

response = client.delete_app_image_config(
    AppImageConfigName='___kernal_config_name___'
)
