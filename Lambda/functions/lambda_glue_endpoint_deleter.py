## This function lists down the active glue-dev-endpoints and deletes them ##

import json
import boto3
import logging


logger = logging.getLogger()
logger.setLevel(logging.INFO)

client = boto3.client('glue')


def return_endpoints():
    endpoints = []
    response = client.list_dev_endpoints()

    # Output the glue endpoints
    for endpoint in response['DevEndpointNames']:
        endpoints.append(endpoint)

    print(f'Found {len(endpoints)} endpoints')
    return endpoints


def terminate_endpoints(event, context):
    print('Starting end-of-week endpoint termination')
    try:
        endpoints = return_endpoints()
        logger.info('Event: %s', event)
        kills = 0
        for endpoint in endpoints:
            client.delete_dev_endpoint(EndpointName=endpoint)
            print(f'Terminated endpoint: {endpoint}')
            kills += 1
        print(
            f'Successfully terminated {kills} endpoints out of total {len(endpoints)} endpoints.')
        response = {
            'statusCode': 200,
            'body': json.dumps(f'Successfully killed {kills} endpoints out of total {len(endpoints)} endpoints.')
        }

        return response

    except Exception as e:
        logger.exception("Couldn't delete endpoint %s because %s", endpoint, e)
