# Use this template to create a dataset

# Reference link
# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client.create_dataset

# Step 2

import boto3
import os

os.environ['AWS_PROFILE'] = "______"
os.environ['AWS_DEFAULT_REGION'] = "______"


# Set ECR as client
client = boto3.client('forecast')

response = client.create_dataset(
    DatasetName='______',
    Domain='___must_match_domain_defined_during_create_dataset_group___',
    DatasetType='TARGET_TIME_SERIES' | 'RELATED_TIME_SERIES' | 'ITEM_METADATA',

    # Valid intervals are Y (Year), M (Month), W (Week), D (Day), H (Hour), 30min (30 minutes), 15min (15 minutes), 10min (10 minutes), 5min (5 minutes), and 1min (1 minute).
    # For example, "D" indicates every day and "15min" indicates every 15 minutes.
    DataFrequency='______',

    # Refer below link to identify required attributes in each domain
    # https://docs.aws.amazon.com/forecast/latest/dg/howitworks-domains-ds-types.html
    Schema={
        'Attributes': [
            {
                'AttributeName': 'string',
                'AttributeType': 'string' | 'integer' | 'float' | 'timestamp' | 'geolocation'
            },
        ]
    },
    Tags=[
        {
            'Key': '______',
            'Value': '______'
        },
    ]
)

print(response)
