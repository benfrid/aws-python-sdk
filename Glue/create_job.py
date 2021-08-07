# Use this template to create Glue jobs in AWS

# Reference link
# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.create_job

import boto3
import os

os.environ['AWS_PROFILE'] = "......"
os.environ['AWS_DEFAULT_REGION'] = "......"

# Set Glue as client
client = boto3.client('glue')


# Glue job parameters:
job_directory = '......'
partition_column = '......'


# Job settings(for additional details on the parameters, use reference link)
response = client.create_job(
    Name='......',
    Description='......',
    Role='......',
    ExecutionProperty={
        'MaxConcurrentRuns': 3
    },
    Command={
        'Name': 'glueetl',
        'ScriptLocation': '......',
        'PythonVersion': '3'
    },
    DefaultArguments={
        '--job-bookmark-option': 'job-bookmark-enable',
        '--enable-continuous-cloudwatch-log': 'true',
        '--enable-continuous-log-filter': 'true',
        '--job_directory': job_directory,
        '--partition_column': partition_column
    },
    Connections={
        'Connections': [
            '......',
        ]
    },
    MaxRetries=3,
    Timeout=2880,
    Tags={
        'created-by': '......'
    },
    GlueVersion='2.0',
    NumberOfWorkers=10,
    WorkerType='G.1X'
)
