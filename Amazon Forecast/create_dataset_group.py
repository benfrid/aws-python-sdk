# Use this template to create a dataset group

# Reference link
# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client.create_dataset_group

# Step 1

import boto3
import os

os.environ['AWS_PROFILE'] = "______"
os.environ['AWS_DEFAULT_REGION'] = "______"


# Set ECR as client
client = boto3.client('forecast')

response = client.create_dataset_group(
    DatasetGroupName='______',
    Domain='RETAIL' | 'CUSTOM' | 'INVENTORY_PLANNING' | 'EC2_CAPACITY' | 'WORK_FORCE' | 'WEB_TRAFFIC' | 'METRICS',
    Tags=[
        {
            'Key': '______',
            'Value': '______'
        },
    ]
)

print(response)
