# Use this template to add the specified targets to the specified rule, or update the targets if they are already associated with the rule

# Reference link
# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events.html#EventBridge.Client.put_targets

import boto3
import os
import logging
from botocore.exceptions import ClientError

logger = logging.getLogger(__name__)

os.environ['AWS_PROFILE'] = "_____"
os.environ['AWS_DEFAULT_REGION'] = "_____"

# Set Glue as client
client = boto3.client('events')


def targets(event_rule_name, lambda_function_name, lambda_function_arn):
    try:
        response = client.put_targets(
            Rule=event_rule_name,
            Targets=[{'Id': lambda_function_name, 'Arn': lambda_function_arn}])
        if response['FailedEntryCount'] > 0:
            logger.error(
                "Couldn't set %s as the target for %s.",
                lambda_function_name, event_rule_name)
        else:
            logger.info(
                "Set %s as the target of %s.", lambda_function_name, event_rule_name)
    except ClientError:
        logger.exception(
            "Couldn't set %s as the target of %s.", lambda_function_name,
            event_rule_name)
        raise


def main():
    event_rule_name = '_____'
    lambda_function_name = '_____'
    lambda_function_arn = '_____'
    targets(event_rule_name, lambda_function_name, lambda_function_arn)


if __name__ == '__main__':
    main()
