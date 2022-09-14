import boto3
ec2 = boto3.client('ec2')
myinstance = ec2.describe_instances(Filters=[{'Name': 'tag:Name', 'Values': ['Jenkins_Built_instance']}]
print(myinstance)