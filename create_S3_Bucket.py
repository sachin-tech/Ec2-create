import boto3
resource = boto3.resource("s3")
bucket_name = "python-sbhing-bucket"
location = {'LocationConstraint'}
bucket = resource.create_bucket(
  Bucket=bucket_name,
  ACL='private')
bucket_tagging = s3.BucketTagging(bucket)
Set_Tag = bucket_tagging.put(Tagging={'TagSet':[{'Key':'Owner', 'Value': 'SB'}], [{'Key':'Env', 'Value': 'Prod'}]})
