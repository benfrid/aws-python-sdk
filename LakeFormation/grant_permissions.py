# Use this template to grant permissions to the principal to access Data Catalog

# Grant permissions to the database and table separately
# For granting permissions to specific columns, use TableWithColumns (from reference link)
# For SSO login, provide permissions to login role along with the execution role


# Reference link
# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lakeformation.html#LakeFormation.Client.grant_permissions


import boto3
import os

os.environ['AWS_PROFILE'] = "______"
os.environ['AWS_DEFAULT_REGION'] = "______"

client = boto3.client('lakeformation')

# Grant permissions to the database
response = client.grant_permissions(
    Principal={
        'DataLakePrincipalIdentifier': '___arn_of_principal___'
    },
    Resource={
        'Database': {
            'Name': '______'
        }
    },
    Permissions=[
        'ALL'
    ],
    PermissionsWithGrantOption=[
        'ALL'
    ]
)

print(response)


# Grant permissions to the table
response = client.grant_permissions(
    Principal={
        'DataLakePrincipalIdentifier': '___arn_of_principal___'
    },
    Resource={
        'Table': {
            'DatabaseName': '______',
            'TableWildcard': {}
        }
    },
    Permissions=[
        'ALL'
    ],
    PermissionsWithGrantOption=[
        'ALL'
    ]
)
