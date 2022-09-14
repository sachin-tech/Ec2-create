#CReating ec2 instance
import boto3
#client = boto3.client(
 #   'ec2',
  #  aws_access_key_id="AKIA4RH4TEY6T7H65CPW",
   # aws_secret_access_key="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"
#)
ec2 = boto3.resource('ec2')
instances = ec2.create_instances(
        ImageId="ami-05fa00d4c63e32376",
        MinCount=1,
        MaxCount=1,
        InstanceType="t2.micro",
        SubnetId="subnet-02b013f38ce974e5c",
        KeyName="dockr_key"
    )
