import boto3
ec2 = boto3.client('ec2')
myinstance = ec2.describe_instances
for instance in myinstance:
  print(instance.id)
