# Use this template to create a predictor in Amazon forecast

# Reference link
# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client.create_predictor

# Step 5.2

# Note: Before you can use the predictor to create a forecast, the Status of the predictor must be ACTIVE , signifying that training has completed.
# To get the status, use the DescribePredictor operation.

import boto3
import os

os.environ['AWS_PROFILE'] = "______"
os.environ['AWS_DEFAULT_REGION'] = "______"


# Set ECR as client
client = boto3.client('forecast')

response = client.create_predictor(
    PredictorName='______',

    #  Required if PerformAutoML is not set to true
    # https://docs.aws.amazon.com/forecast/latest/dg/aws-forecast-choosing-recipes.html
    AlgorithmArn='______',

    # The maximum forecast horizon is the lesser of 500 time-steps or 1/3 of the TARGET_TIME_SERIES dataset length
    ForecastHorizon=12,

    # Optional: Forecast types can be quantiles from 0.01 to 0.99, by increments of 0.01 or higher. The default value is ["0.10", "0.50", "0.9"]
    ForecastTypes=[
        '______',
    ],

    # Optional: The default value is FALSE. This is a good option if you aren't sure which algorithm is suitable for your training data
    # Note: If set TRUE, set PerformHPO to FALSE
    # When AutoML is enabled, the following properties are disallowed:
    # AlgorithmArn
    # HPOConfig
    # PerformHPO
    # TrainingParameters
    PerformAutoML=True | False,

    # Optional: The default value is false . In this case, Amazon Forecast uses default hyperparameter values from the chosen algorithm
    # If set TRUE, make PerformAutoML as FALSE and provide the HPOConfig measures
    # Note: Only DeepAR+ and CNN-QR supports HPO
    PerformHPO=True | False,

    # Optional: default AutoML strategy
    # Note: Only valid for predictors trained using AutoML
    # Default is AccuracyOptimized. LatencyOptimized is still in BETA phase
    AutoMLOverrideStrategy='LatencyOptimized' | 'AccuracyOptimized',

    # Optional: The hyperparameters to override for model training. The hyperparameters that you can override are listed in the individual algorithms
    # https://docs.aws.amazon.com/forecast/latest/dg/aws-forecast-choosing-recipes.html
    TrainingParameters={
        'string': 'string'
    },

    # Optional
    EvaluationParameters={
        # The number of times to split the input data. The default is 1. Valid values are 1 through 5
        'NumberOfBacktestWindows': 123,
        # Specify the value as the number of data points for back-testing. The default is the value of the forecast horizon
        # This value must be greater than or equal to the forecast horizon and less than half of the TARGET_TIME_SERIES dataset length
        'BackTestWindowOffset': 123
    },

    # Optional: Provides hyperparameter override values for the algorithm. If you don't provide this parameter, Amazon Forecast uses default values.
    HPOConfig={
        'ParameterRanges': {
            'CategoricalParameterRanges': [
                {
                    'Name': '______',
                    'Values': [
                        '______',
                    ]
                },
            ],
            'ContinuousParameterRanges': [
                {
                    'Name': '______',
                    'MaxValue': 123.0,
                    'MinValue': 123.0,
                    'ScalingType': 'Auto' | 'Linear' | 'Logarithmic' | 'ReverseLogarithmic'
                },
            ],
            'IntegerParameterRanges': [
                {
                    'Name': '______',
                    'MaxValue': 123,
                    'MinValue': 123,
                    'ScalingType': 'Auto' | 'Linear' | 'Logarithmic' | 'ReverseLogarithmic'
                },
            ]
        }
    },

    # Describes the dataset group that contains the data to use to train the predictor
    InputDataConfig={
        'DatasetGroupArn': '______'
    },

    FeaturizationConfig={
        # Valid intervals are Y (Year), M (Month), W (Week), D (Day), H (Hour), 30min (30 minutes), 15min (15 minutes), 10min (10 minutes), 5min (5 minutes), and 1min (1 minute).
        # For example, "Y" indicates every year and "5min" indicates every five minutes.
        'ForecastFrequency': '______',

        # Optional: item_id is added by default
        'ForecastDimensions': [
            'string',
        ]
    },
    Tags=[
        {
            'Key': '______',
            'Value': '______'
        },
    ],

    # Optional
    OptimizationMetric='WAPE' | 'RMSE' | 'AverageWeightedQuantileLoss' | 'MASE' | 'MAPE'
)

print(response)
