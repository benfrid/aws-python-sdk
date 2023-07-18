# Use this template to grant an AWS service or another account permission to use a function.
# Here, we grant EventBridge CloudWatch events the required permissions

# Reference link
# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lambda.html#Lambda.Client.add_permission

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


def lambda_add_permission(lambda_function_name, event_rule_arn):
    try:
        client.add_permission(
            FunctionName=lambda_function_name,
            StatementId=f'{lambda_function_name}-invoke',
            Action='lambda:InvokeFunction',
            Principal='events.amazonaws.com',
            SourceArn=event_rule_arn
        )
        logger.info(
            "Granted permission to let Amazon EventBridge call function %s",
            lambda_function_name)
    except ClientError:
        logger.exception(
            "Couldn't add permission to let Amazon EventBridge call function %s.",
            lambda_function_name)
        raise


def main():
    lambda_function_name = '_____'
    event_rule_arn = '_____'
    lambda_add_permission(lambda_function_name, event_rule_arn)


if __name__ == '__main__':
    main()
