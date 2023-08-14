import boto3

# Set your AWS credentials and region here
aws_access_key = 'AKIA6JFGOQQ2UEOL2POT'
aws_secret_key = '4zF282eA9/iDM0J/958O91OSiImOlP7inFMRLB9S'
aws_region = 'us-east-1'

# Initialize the EC2 client
ec2 = boto3.client('ec2', region_name=aws_region, aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key)

# Create a new EC2 instance
"""
response = ec2.run_instances(
    ImageId='ami-09538990a0c4fe9be',  # Replace with the desired AMI ID
    InstanceType='t2.micro',
    MinCount=1,
    MaxCount=1
  
    
)
"""

# Print the instance ID of the newly created instance
#instance_id = response['Instances'][0]['InstanceId']
instance_id="i-06060ced11f2a2f54"
print(f"New EC2 instance created with ID: {instance_id}")


# Stop the instance
instance_id_to_stop=instance_id
response = ec2.stop_instances(InstanceIds=[instance_id_to_stop])

# Print the response
print(f"Stopping instance {instance_id_to_stop}: {response}")