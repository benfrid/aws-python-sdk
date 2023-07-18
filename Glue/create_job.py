# Use this template to create Glue jobs in AWS

# Reference link
# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.create_job

import boto3
import os

os.environ['AWS_PROFILE'] = "______"
os.environ['AWS_DEFAULT_REGION'] = "______"

# Set Glue as client
client = boto3.client('glue')


# Glue job parameters:
job_directory = '______'
partition_column = '______'


# Job settings(for additional details on the parameters, use reference link)
response = client.create_job(
    Name='______',
    Description='______',
    Role='______',
    ExecutionProperty={
        'MaxConcurrentRuns': 3
    },
    Command={
        'Name': 'glueetl',
        'ScriptLocation': '______',
        'PythonVersion': '3'
    },
    DefaultArguments={
        '--TempDir': "______",
        '--job-bookmark-option': 'job-bookmark-enable',
        '--enable-continuous-cloudwatch-log': 'true',
        '--enable-continuous-log-filter': 'true',
        '--job_directory': job_directory,
        '--partition_column': partition_column,
        '--additional-python-modules': '______'
    },
    Connections={
        'Connections': [
            '______',
        ]
    },
    MaxRetries=0,
    Timeout=2880,
    Tags={
        '__Key__': '__Value__'
    },
    GlueVersion='3.0',
    NumberOfWorkers=10,
    WorkerType='G.1X'
)
