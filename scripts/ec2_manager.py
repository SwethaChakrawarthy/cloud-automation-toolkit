# scripts/ec2_manager.py

from utils.boto3_session import get_boto3_session

def launch_instance():
    ec2 = get_boto3_session('ec2')

    try:
        response = ec2.run_instances(
            ImageId='ami-0c02fb55956c7d316',  # Amazon Linux 2 AMI (for us-east-1)
            InstanceType='t2.micro',
            MinCount=1,
            MaxCount=1,
            KeyName='toolkit',  # Replace with your key pair name
            SecurityGroups=['default'],   # Or replace with your security group
            TagSpecifications=[
                {
                    'ResourceType': 'instance',
                    'Tags': [{'Key': 'Project', 'Value': 'CloudToolkit'}]
                }
            ]
        )

        instance_id = response['Instances'][0]['InstanceId']
        print(f"[EC2] Launched instance: {instance_id}")
        return instance_id

    except Exception as e:
        print(f"[EC2] Error launching instance: {e}")
