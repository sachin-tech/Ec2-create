import boto3
ec2 = boto3.resource('ec2', 'us-east-1')
myinstance = ec2_describe.instances
print(myinstance)
