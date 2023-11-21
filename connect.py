from local_secrets import user
import boto3

session = boto3.Session(
    aws_access_key_id = user.public_key,
    aws_secret_access_key = user.secret_key
)

s3 = session.resource('s3')

for bucket in s3.buckets.all():
    print(bucket.name)