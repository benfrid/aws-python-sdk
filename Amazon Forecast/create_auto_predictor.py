# Use this template to create an auto predictor in Amazon forecast

# Reference link
# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client.create_auto_predictor

# Step 5.1


import boto3
import os

os.environ['AWS_PROFILE'] = "______"
os.environ['AWS_DEFAULT_REGION'] = "______"


# Set ECR as client
client = boto3.client('forecast')

response = client.create_auto_predictor(
    PredictorName='______',

    # Note: The dataset must be atleast 4 times the forecast horizon
    ForecastHorizon=123,

    # Optional: Forecast types can be quantiles from 0.01 to 0.99, by increments of 0.01 or higher. The default value is ["0.10", "0.50", "0.9"]
    ForecastTypes=[
        '______',
    ],

    # The frequency must be greater than or equal to the TARGET_TIME_SERIES dataset frequency
    # Valid intervals are Y (Year), M (Month), W (Week), D (Day), H (Hour), 30min (30 minutes), 15min (15 minutes), 10min (10 minutes), 5min (5 minutes), and 1min (1 minute).
    # For example, "Y" indicates every year and "5min" indicates every five minutes.
    ForecastFrequency='______',

    DataConfig={
        'DatasetGroupArn': '______',

        # Refer API link
        'AttributeConfigs': [
            {
                'AttributeName': '______',
                'Transformations': {
                    '______': '______'
                }
            },
        ]
    },

    # Optional: The ARN of the predictor to retrain or upgrade
    ReferencePredictorArn='______',

    # Optional
    OptimizationMetric='WAPE' | 'RMSE' | 'AverageWeightedQuantileLoss' | 'MASE' | 'MAPE',

    # Optional: Create an Explainability resource for the predictor.
    ExplainPredictor=True | False,
    Tags=[
        {
            'Key': '______',
            'Value': '______'
        },
    ]
)

print(response)
