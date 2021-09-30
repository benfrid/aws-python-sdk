# Use this template to list the names of all DevEndpoint resources in the account, or the resources with the specified tag.

# Reference link
# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client.list_dev_endpoints

import boto3
import os

os.environ['AWS_PROFILE'] = "_____"
os.environ['AWS_DEFAULT_REGION'] = "_____"

# Set Glue as client
client = boto3.client('glue')

response = client.list_dev_endpoints()

# Output the glue endpoints
print('Existing glue endpoints:')
for endpoint in response['DevEndpointNames']:
    print(f'  {endpoint}')
