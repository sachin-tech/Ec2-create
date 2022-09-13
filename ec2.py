import boto3
ec2 = boto3.resource('ec2')
instances = ec2.create_instances(
        ImageId=" ami-05fa00d4c63e32376",
        MinCount=1,
        MaxCount=1,
        InstanceType="t2.micro",
        KeyName="dockr_key"
    )
