import boto3
import os
import json

os.environ['AWS_PROFILE'] = "______"
os.environ['AWS_DEFAULT_REGION'] = "______"

# Set Glue as client
client = boto3.client('glue')

# This policy puts Glue resource policy to enable both Tag based as well as Named Catalog sharing
policy = {
  "Version" : "2012-10-17",
  "Statement" : [ {
    "Effect" : "Allow",
    "Principal" : {
      "AWS" : "arn:aws:iam::<customer_account_id>:root"
    },
    "Action" : "glue:*",
    "Resource" : [ "arn:aws:glue:<region>:<producer_account_id>:table/*", "arn:aws:glue:<region>:producer_account_id:database/*", "arn:aws:glue:<region>:producer_account_id:catalog" ],
    "Condition" : {
      "Bool" : {
        "glue:EvaluatedByLakeFormationTags" : "true"
      }
    }
  },
      {
      "Effect": "Allow",
      "Action": [
        "glue:ShareResource"
      ],
      "Principal": {"Service": [
        "ram.amazonaws.com"
      ]},
      "Resource": [
        "arn:aws:glue:<region>:producer_account_id:table/*/*",
        "arn:aws:glue:<region>:producer_account_id:database/*",
        "arn:aws:glue:<region>:producer_account_id:catalog"
      ]
    } ] 
}


policy_str = json.dumps(policy)
client.put_resource_policy(PolicyInJson=policy_str, EnableHybrid='TRUE')