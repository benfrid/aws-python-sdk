"""
Use this template to return a create a new S3 bucket. Additional bucket configurations include,
    - Bucket tags
    - No delete bucket policy
    - SSE-S3 bucket encryption
    - Block public access rules
    - Versioning & lifecycle configuration
"""

# Reference link
# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#id221

import boto3
import os
import json
import logging
from botocore.exceptions import ClientError

logger = logging.getLogger(__name__)

os.environ['AWS_PROFILE'] = "______"
os.environ['AWS_DEFAULT_REGION'] = "______"


# Set S3 as resource
client = boto3.client('s3')
resource = boto3.resource('s3')
region = boto3.Session().region_name

# Set STS as client to get the account ID
sts_client = boto3.client('sts')
sts_response = sts_client.get_caller_identity()


def create_bucket(bucket_name, region=None):
    """
    Creates an S3 bucket in the region specified

    :param bucket_name: The name of the bucket to create
    :param region: Identifies the region to create the bucket
    :return: The newly created bucket
    """
    try:
        if region:
            bucket = resource.create_bucket(
                Bucket=bucket_name,
                CreateBucketConfiguration={
                    'LocationConstraint': region
                }
            )
        else:
            bucket = resource.create_bucket(Bucket=bucket_name)

        bucket.wait_until_exists()

        logger.info("Created bucket '%s' in region=%s", bucket_name,
                    resource.meta.client.meta.region_name)
    except ClientError as error:
        logger.exception("Couldn't create bucket named '%s' in region=%s.",
                         bucket_name, region)
        if error.response['Error']['Code'] == 'IllegalLocationConstraintException':
            logger.error("When the session Region is anything other than us-east-1, "
                         "you must specify a LocationConstraint that matches the "
                         "session Region. The current session Region is %s and the "
                         "LocationConstraint Region is %s.",
                         resource.meta.client.meta.region_name, region)
        raise error
    else:
        return bucket


def tag_bucket(bucket_name):
    """
    Add custom tags to the bucket

    :param bucket_name: The name of the bucket to apply configuration
    :return: response
    """
    bucket_tagging = resource.BucketTagging(bucket_name)
    response = bucket_tagging.put(
        Tagging={
            'TagSet': [
                {
                    'Key': '______',
                    'Value': '______',
                },
                {
                    'Key': '______',
                    'Value': '______'
                }
            ]
        })
    return response


def specify_bucket_policy(bucket_name):
    """
    Define no-delete bucket policy

    :param bucket_name: The name of the bucket to apply configuration
    :return: response
    """
    # The policy must be in JSON format.
    bucket_policy = {
        'Version': '2012-10-17',
        'Statement': [{
            'Sid': 'DoNotAllowBucketDelete',
            'Effect': 'Deny',
            'Principal': '*',
            'Action': ['s3:DeleteBucket'],
            'Resource': f'arn:aws:s3:::{bucket_name}'
        }]
    }
    return bucket_policy


def put_policy(bucket_name):
    """
    Add no-delete bucket policy to the bucket

    :param bucket_name: The name of the bucket to apply configuration
    :return: response
    """
    # Define the bucket policy to be used
    policy = specify_bucket_policy(bucket_name)
    try:
        resource.Bucket(bucket_name).Policy().put(Policy=json.dumps(policy))
        logger.info("Put policy %s for bucket '%s'.", policy, bucket_name)
    except ClientError:
        logger.exception("Couldn't apply policy to bucket '%s'.", bucket_name)
        raise


def put_encryption(bucket_name):
    """
    Add S3-SSE encryption to the bucket

    :param bucket_name: The name of the bucket to apply configuration
    :return: response
    """
    response = client.put_bucket_encryption(
        Bucket=bucket_name,
        ServerSideEncryptionConfiguration={
            'Rules': [
                {
                    'ApplyServerSideEncryptionByDefault': {
                        'SSEAlgorithm': 'AES256'
                    }
                },
            ]
        })
    return response


def put_access_block(bucket_name):
    """
    Block all public access to the bucket

    :param bucket_name: The name of the bucket to apply configuration
    :return: response
    """
    response = client.put_public_access_block(
        Bucket=bucket_name,
        PublicAccessBlockConfiguration={
            'BlockPublicAcls': True,
            'IgnorePublicAcls': True,
            'BlockPublicPolicy': True,
            'RestrictPublicBuckets': True
        })
    return response


def versioning(bucket_name, expiration):
    """
    Enable versioning and set lifecycle configuration to expire old versions

    :param bucket_name: The name of the bucket to apply configuration
    :param expiration: Set the expiration duration (in days)
    :return: response
    """
    try:
        response = client.put_bucket_versioning(
            Bucket=bucket_name,
            VersioningConfiguration={
                'MFADelete': 'Disabled',
                'Status': 'Enabled'
            })
        logger.info("Enabled versioning on bucket %s.", bucket_name)
    except ClientError:
        logger.exception(
            "Couldn't enable versioning on bucket %s.", bucket_name)
        raise

    try:
        response = client.put_bucket_lifecycle_configuration(
            Bucket=bucket_name,
            LifecycleConfiguration={
                'Rules': [
                    {
                        'Status': 'Enabled',
                        'Filter': {'Prefix': ''},
                        'NoncurrentVersionExpiration': {
                            'NoncurrentDays': expiration
                        }
                    }]
            })
        logger.info("Configured lifecycle to expire noncurrent versions after %s days "
                    "on bucket %s.", expiration, bucket_name)
    except ClientError as error:
        logger.warning("Couldn't configure lifecycle on bucket %s because %s. "
                       "Continuing anyway.", bucket_name, error)

    return response


def main():
    bucket_name = '______' + sts_response['Account']

    # Create the S3 bucket in the specified region
    bucket = create_bucket(bucket_name, region)
    print(f'Created bucket {bucket.name}')
    logger.info("Created bucket %s", bucket.name)

    # Select the below parameters as required (comment otherwise)
    # Tag the created bucket
    tag_bucket(bucket_name)
    print(f'Configured tags on bucket {bucket.name}')
    logger.info("Configured tags on bucket %s", bucket.name)

    # Add bucket encryption
    put_encryption(bucket_name)
    print(f'Configured encryption on bucket {bucket.name}')
    logger.info("Configured encryption on bucket %s", bucket.name)

    # Add public access blockers
    put_access_block(bucket_name)
    print(f'Configured public access policy on bucket {bucket.name}')
    logger.info("Configured public access policy on bucket %s", bucket.name)

    # Add bucket versioining and lifecycle rule set to expire after a year
    versioning(bucket_name, 365)
    print(f'Configured versioning & lifecycle policy on bucket {bucket.name}')
    logger.info(
        "Configured versioning & lifecycle policy on bucket %s", bucket.name)

    # Put the no-delete bucket policy
    put_policy(bucket_name)
    print(f'Configured bucket policy on bucket {bucket.name}')
    logger.info("Configured bucket policy on bucket %s", bucket.name)

    print("Action completed!")


if __name__ == '__main__':
    main()
