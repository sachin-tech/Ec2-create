import boto3
ec2 = boto3.resource('ec2')
instances = ec2.create_instances(
        ImageId="ami-05fa00d4c63e32376",
        VPCId="vpc-06e2337457b5130b5",
        MinCount=1,
        MaxCount=1,
        InstanceType="t2.micro",
        KeyName="dockr_key"
    )
