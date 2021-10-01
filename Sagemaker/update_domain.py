# Use this template to update the default settings for new user profiles in the domain.
# Step IV

# Reference link
# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.update_domain

import boto3
import os

os.environ['AWS_PROFILE'] = "_____"
os.environ['AWS_DEFAULT_REGION'] = "_____"


# Set ECR as client
client = boto3.client('sagemaker')

response = client.update_domain(
    DomainId='___studio_id___',
    DefaultUserSettings={
        "KernelGatewayAppSettings": {
            "CustomImages": [
                {
                    "ImageName": "___image_name_from_step_I___",
                    "AppImageConfigName": "___kernal_config_name_from_step_III___"
                }
            ]
        }
    }
)

print(response)
