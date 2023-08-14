#import Modules
import boto3
# Set your AWS credentials and region here
aws_access_key = 'AKIA6JFGOQQ2UEOL2POT'
aws_secret_key = '4zF282eA9/iDM0J/958O91OSiImOlP7inFMRLB9S'
aws_region = 'us-east-1'

# Initialize the EC2 client
ec2 = boto3.client('ec2', region_name=aws_region, aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key)

#variables
instance_id = [ "i-06060ced11f2a2f54", "i-0c1b413b0d4c05beb" ]

#reboot Logic
#Functions
def reboot(id):
    response = ec2.reboot_instances(InstanceIds=[id,],DryRun=False)
    responsecode = response['ResponseMetadata']['HTTPStatusCode']
    if responsecode == 200:
        print ("Instance ID: {} is rebooted".format(id))
        print ("\n")
    else:
        print ("Instance ID: {} failed to reboot".format(id))
reboot(instance_id[0])
reboot(instance_id[1])