# scripts/iam_manager.py

from utils.boto3_session import get_boto3_session
import json

def create_iam_role(role_name, assume_policy_path):
    iam = get_boto3_session('iam')

    try:
        with open(assume_policy_path) as f:
            assume_policy = json.load(f)

        response = iam.create_role(
            RoleName=role_name,
            AssumeRolePolicyDocument=json.dumps(assume_policy),
            Description='Role for Cloud Automation Toolkit'
        )

        print(f"[IAM] Role created: {role_name}")
        return response['Role']['Arn']

    except Exception as e:
        print(f"[IAM] Error creating role: {e}")
