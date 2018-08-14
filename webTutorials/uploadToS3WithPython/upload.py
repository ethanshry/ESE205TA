import boto3
session = boto3.Session(
    aws_access_key_id='',
    aws_secret_access_key='',
)
s3 = session.resource('s3', region_name='us-east-1')
object = s3.Object('bucket-name', 'sampleUpload.txt')
object.put(Body=open('./sampleUpload.txt', 'rb'))