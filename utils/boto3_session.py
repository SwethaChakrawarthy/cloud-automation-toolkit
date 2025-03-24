# utils/boto3_session.py

import boto3
import os
from dotenv import load_dotenv

load_dotenv()

def get_boto3_session(service_name, region_name='us-east-1'):
    return boto3.client(
        service_name,
        aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
        region_name=region_name
    )

