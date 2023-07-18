# Use this template to create a Lambda function. To create a function, you need a deployment package and an execution role .

# Reference link
# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lambda.html#Lambda.Client.create_function

import boto3
import os
import io
import zipfile
import logging
from botocore.exceptions import ClientError

logger = logging.getLogger(__name__)

os.environ['AWS_PROFILE'] = "_____"
os.environ['AWS_DEFAULT_REGION'] = "_____"

# Set Glue as client
client = boto3.client('lambda')


def create_lambda_deployment_package(function_file_name):
    """
    Creates a Lambda deployment package in ZIP format in an in-memory buffer. This
    buffer can be passed directly to AWS Lambda when creating the function.

    :param function_file_name: The name of the file that contains the Lambda handler function.
    :return: The deployment package.
    """
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, 'w') as zipped:
        zipped.write(function_file_name)
    buffer.seek(0)
    return buffer.read()


def deploy_lambda_function(function_name, handler_name, iam_role, deployment_package, run_time):
    try:
        response = client.create_function(
            FunctionName=function_name,
            Description='______',
            Runtime=run_time,
            Handler=handler_name,
            Role=iam_role,
            Code={
                'ZipFile': deployment_package},
            Tags={
                'Key': 'Value'
            })
        function_arn = response['FunctionArn']
        logger.info("Created function '%s' with ARN: '%s'.",
                    function_name, response['FunctionArn'])
    except ClientError:
        logger.exception("Couldn't create function %s.", function_name)
        raise
    else:
        return function_arn


def main():
    lambda_function_filename = '__sample_function.py__'
    lambda_handler_name = '__sample_function.lambda_handler__'
    lambda_role_name = '__lambda_role_with_access_to_services__'
    lambda_function_name = '_____'
    lambda_run_time = '__python3.9__'

    # Package the lambda function python file as Zip
    deployment_package = create_lambda_deployment_package(
        lambda_function_filename)

    deploy_lambda_function(lambda_function_name,
                           lambda_handler_name, lambda_role_name, deployment_package, lambda_run_time)


if __name__ == '__main__':
    main()
