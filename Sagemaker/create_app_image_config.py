# Use this template to creates a configuration for running a SageMaker image as a KernelGateway app.
# Step III

# Reference link
# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_app_image_config

import boto3
import os

os.environ['AWS_PROFILE'] = "_____"
os.environ['AWS_DEFAULT_REGION'] = "_____"


# Set ECR as client
client = boto3.client('sagemaker')

response = client.create_app_image_config(
    AppImageConfigName='___kernal_config_name___',
    Tags=[
        {
            'Key': '_____',
            'Value': '_____'
        },
    ],
    KernelGatewayImageConfig={
        'KernelSpecs': [
            {
                'Name': 'conda-env-custom-mlenv-py',
                'DisplayName': '___kernel_display_name_in_studio___'
            },
        ],
        'FileSystemConfig': {
            'MountPath': '/root',
            'DefaultUid': 0,
            'DefaultGid': 0
        }
    }
)

print(response)
