## Scenario -1  List Instance Ids
import boto3
# Set your AWS credentials and region here
aws_access_key = 'AKIA6JFGOQQ2UEOL2POT'
aws_secret_key = '4zF282eA9/iDM0J/958O91OSiImOlP7inFMRLB9S'
aws_region = 'us-east-1'

# Initialize the EC2 client
ec2 = boto3.client('ec2', region_name=aws_region, aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key)

instances = ec2.describe_instances()
print(instances)
i=len(instances['Reservations'])
print("number of ec2",i)
for item in range(0,i):
    for instance in instances['Reservations'][item]['Instances']:
        print (instance['InstanceId'])
"""
## Scenario -2 List Name Tag of EC2 Instances
import boto3
ec2 = boto3.client('ec2')
instances = ec2.describe_instances()
for instance in instances['Reservations'][0]['Instances']:
    InstanceId = instance['InstanceId']
    for tags in instance['Tags']:
        if tags['Key'] == "Name":
            value = tags['Value']
            print ("Instance Id: {} and Tag Name: {}".format(InstanceId, value))
"""