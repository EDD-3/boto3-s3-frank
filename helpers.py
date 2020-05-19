import boto3, botocore
from config import S3_KEY, S3_SECRET, S3_BUCKET
from botocore.client import Config
from app import app
from uuid import uuid4
from PIL import Image
import io
import binascii

s3_resource = boto3.resource(
    's3',
     aws_access_key_id=S3_KEY,
     aws_secret_access_key=S3_SECRET,
     config=Config(signature_version='s3v4')
     )

'''
s3 = boto3.client(
   "s3",
   aws_access_key_id=S3_KEY,
   aws_secret_access_key=S3_SECRET,
)
'''

def upload_file_to_s3(response, bucket_name, acl="public-read"):

    try:
        file_data = response.read() 
        file_extension = response.getheader('Content-Type').split('/')[-1].lower()
        file_name = f'{uuid4().hex}.{file_extension}'
        s3_resource.Bucket(bucket_name).put_object(Key=file_name, Body=file_data, ACL='public-read')

    except Exception as e:
        print("Exception: ", e)
        return e

    return "{}{}".format(app.config["S3_LOCATION"],file_name)