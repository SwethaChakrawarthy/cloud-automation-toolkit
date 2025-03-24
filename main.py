# main.py

from scripts.ec2_manager import launch_instance
from scripts.s3_manager import create_bucket
from scripts.iam_manager import create_iam_role

if __name__ == "__main__":
    print("🔧 Cloud Automation Toolkit - Starting...\n")

    # Step 1: Create S3 Bucket
    bucket_name = "my-cloud-toolkit-bucket-12345"  # Must be globally unique
    create_bucket(bucket_name)

    # Step 2: Launch EC2 Instance
    launch_instance()

    # Step 3: Create IAM Role
    create_iam_role("CloudToolkitRole", "config/iam_policies/assume_role.json")

    print("\n✅ Automation Complete.")
