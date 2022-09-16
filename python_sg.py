import boto3
from botocore.exceptions import ClientError
AWS_REGION = 'us-east-1'
vpc_resource = boto3.resource("ec2", region_name=AWS_REGION)
response = boto3.describe_vpcs()
vpc_id = response.get('Vpcs', [{}])[0].get('VpcId', '')
try:
      response = ec2.create_securitygroup(GroupName='python_sg', Description='created using python', VpcId=vpc_id, region='us-east-1')
      security_group_id = response['GroupId']
      print('Security Group Created %s in vpc %s.' % (security_group_id, vpc_id))
      
      data = ec2.authorize_security_group_ingress(
        GroupId = security_group_id,
        IpPermission=[
           {'IpProtocol': 'tcp',
            'FromPort': 80,
            'ToPort': 80,
            'IpRanges': [{'CidrIp': '0.0.0.0/0'}]},
           {'IpProtocol': 'tcp',
            'FromPort': 22,
            'IpRanges': [{'CidrIp': '0.0.0.0/0'}]}
        ])
      print('Ingress Successfully Set %s' % data)
except ClientError as e:
 print(e)            
