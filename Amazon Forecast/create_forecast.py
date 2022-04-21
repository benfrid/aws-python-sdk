# Use this template to create a forecast in Amazon forecast

# Reference link
# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client.create_forecast

import boto3
import os

os.environ['AWS_PROFILE'] = "______"
os.environ['AWS_DEFAULT_REGION'] = "______"


# Set ECR as client
client = boto3.client('forecast')

response = client.create_forecast(
    ForecastName='______',
    PredictorArn='______',

    # Optional: You can currently specify up to 5 quantiles per forecast . Accepted values include 0.01 to 0.99
    # The default value is ["0.1", "0.5", "0.9"]
    ForecastTypes=[
        '__forecast_quantiles__',
    ],
    Tags=[
        {
            'Key': '______',
            'Value': '______'
        },
    ]
)

print(response)
