import boto3
ec2 = boto3.resource('ec2', 'us-east-1')
myinstance = ec2-describe.instances(Filters=[{'Name': 'tag:Name', 'Values': ['Jenkins_Built_instance']}])
print(myinstance)
