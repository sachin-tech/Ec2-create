#This code is to create s3 and list using python boto3 and github
import boto3
resource = boto3.resource("s3")
bucket_name = "python-sbhing-bucket"
location = {'LocationConstraint'}
bucket = resource.create_bucket(
  Bucket=bucket_name,
  ACL='private')
bucket_tagging = resource.BucketTagging(bucket_name)
Set_Tag = bucket_tagging.put(Tagging={'TagSet':[{'Key':'Owner', 'Value': 'SB'}]})

s3 = boto3.client("s3")
response = s3.list_buckets()['Buckets']
for bucket in response:
  out = print('Bucket name: {}, Created on: {}'.format(bucket['Name'], bucket['CreationDate']))
  print(out)
