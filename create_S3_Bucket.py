import boto3
resource = boto3.resource("s3"))
bucket_name = "python_created_bucket"
location = {'LocationConstraint'}
bucket = resource.create_bucket(
  Bucket=bucket_name,
  ACL='private')
response2 = resource.put_bucket_tagging(
  Bucket=bucket_name,
  Tagging={
    'TagSet': [
        {
            'Key': 'Name',
            'Value': 'python_script_bucket'
        }
    ]
})
