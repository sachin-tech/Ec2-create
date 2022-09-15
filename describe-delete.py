import boto3
#ec2 = boto3.client('ec2')
#myinstance = ec2.describe_instances()
ec2 = boto3.resource('ec2')
instancename = ''
for tags in ec2instance.tags:
   if tags[“Key”] == ‘Name’:
      instancename = tags[“Value”]
      print(instancename)

