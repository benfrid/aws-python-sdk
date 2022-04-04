# Use this template to list the datasets in Amazon forecast

# Reference link
# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client.list_datasets

import boto3
import os

os.environ['AWS_PROFILE'] = "______"
os.environ['AWS_DEFAULT_REGION'] = "______"


# Set ECR as client
client = boto3.client('forecast')

response = client.list_datasets()

print(response)
