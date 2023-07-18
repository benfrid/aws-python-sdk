# Use this template to list permissions assigned to a principal for a Data Catalog

# Reference link
# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lakeformation.html#LakeFormation.Client.list_permissions


import boto3
import os

os.environ['AWS_PROFILE'] = "______"
os.environ['AWS_DEFAULT_REGION'] = "______"

client = boto3.client('lakeformation')

# List permissions on database
response = client.list_permissions(
    Principal={
        'DataLakePrincipalIdentifier': '___arn_of_principal___'
    },
    Resource={
        'Database': {
            'Name': '______'
        }
    }
)

print(response)

print('\n')

# List permissions on table
response = client.list_permissions(
    Principal={
        'DataLakePrincipalIdentifier': '___arn_of_principal___'
    },
    Resource={
        'Table': {
            'DatabaseName': '______',
            'TableWildcard': {}
        }
    }
)

print(response)
