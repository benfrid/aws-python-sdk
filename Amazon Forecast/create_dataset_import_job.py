# Use this template to create a dataset import job

# Reference link
# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client.create_dataset_import_job

# Step 3

import boto3
import os

os.environ['AWS_PROFILE'] = "______"
os.environ['AWS_DEFAULT_REGION'] = "______"


# Set ECR as client
client = boto3.client('forecast')

response = client.create_dataset_import_job(
    DatasetImportJobName='______',
    DatasetArn='____arn_of_the_dataset_to_import_to____',
    DataSource={
        'S3Config': {
            'Path': '______',
            'RoleArn': '______'
        }
    },

    # The format that you specify depends on the DataFrequency specified when the dataset was created in step 2
    # "yyyy-MM-dd" For the following data frequencies: Y, M, W, and D
    # "yyyy-MM-dd HH:mm:ss" For the following data frequencies: H, 30min, 15min, and 1min; and optionally, for: Y, M, W, and D
    # If the format isn't specified, Amazon Forecast expects the format to be "yyyy-MM-dd HH:mm:ss".
    TimestampFormat='string',
    TimeZone='string',
    Tags=[
        {
            'Key': '______',
            'Value': '______'
        },
    ]
)

print(response)
