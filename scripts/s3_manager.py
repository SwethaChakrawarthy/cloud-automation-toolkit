# scripts/s3_manager.py

from utils.boto3_session import get_boto3_session

def create_bucket(bucket_name):
    s3 = get_boto3_session('s3')
    region = 'us-east-1'

    try:
        if region == 'us-east-1':
            s3.create_bucket(Bucket=bucket_name)
        else:
            s3.create_bucket(
                Bucket=bucket_name,
                CreateBucketConfiguration={'LocationConstraint': region}
            )

        print(f"[S3] Bucket created: {bucket_name}")
    except Exception as e:
        print(f"[S3] Error creating bucket: {e}")
