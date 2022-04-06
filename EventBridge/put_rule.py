# Use this template to create or update the specified rule.

# Reference link
# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events.html#EventBridge.Client.put_rule

import boto3
import os
import logging
from botocore.exceptions import ClientError

logger = logging.getLogger(__name__)

os.environ['AWS_PROFILE'] = "_____"
os.environ['AWS_DEFAULT_REGION'] = "_____"

# Set Glue as client
client = boto3.client('events')


def create_scheduled_event_rule(event_rule_name, event_schedule):
    try:
        response = client.put_rule(
            Name=event_rule_name,
            Description='_____',
            ScheduleExpression=event_schedule,
            Tags=[
                {
                    'Key': '_____',
                    'Value': '_____'
                },
            ])
    except ClientError:
        logger.exception("Couldn't put rule %s.", event_rule_name)
        raise

    return response['RuleArn']


def main():
    event_rule_name = '_____'
    event_schedule = '___rate_or_cron___'
    arn = create_scheduled_event_rule(event_rule_name, event_schedule)
    print(arn)


if __name__ == '__main__':
    main()
