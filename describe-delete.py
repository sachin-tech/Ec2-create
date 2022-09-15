import boto3
ec2 = boto3.client('ec2')
myinstance = ec2.describe_instances()
ec1 = boto3.resource('ec2',"us-east-1")
instances = ec2.instances.filter(Filters=[{'Name': 'Name', 'Values': ['Jenkins_Built_instance']}])
for instance in instances:
   if instance.tags != None:
      for tags in instance.tags:
        if tags["Key"] == 'Name':
          instancename = tags["Value"]
          print("Inastance Name - %s,  Instance Id - %s, Owner - %s " %(instancename,instance.id,owner))
