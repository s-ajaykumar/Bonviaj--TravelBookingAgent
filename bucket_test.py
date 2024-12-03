import boto3
import config

s3 = boto3.resource('s3', aws_access_key_id = config.ACCESS_KEY, aws_secret_access_key = config.SECRET_KEY)

try:
    bucket = s3.Bucket('bonviaj-conversations-bucket')
    objects = list(bucket.objects.all())
    for i in objects:
        print(i.key, "\n")
except:
    print("fuck")