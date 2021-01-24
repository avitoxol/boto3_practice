import boto3

aws_mgt = boto3.session.Session(profile_name = "avitoxol")
s3_cli = aws_mgt.client(service_name = "s3", region_name = "us-east-1")

s3_cli.create_bucket(
        ACL='private',
        Bucket='my-very-test-bucket-012421-8888',
        )

listing = s3_cli.list_buckets()

names = listing['Buckets']

for name in names:
    print(name['Name']
