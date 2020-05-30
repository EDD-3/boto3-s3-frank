import boto3, botocore
from botocore.client import Config
from uuid import uuid4
from api import app

s3_resource = boto3.resource(
    's3',
     aws_access_key_id=app.config['S3_KEY'],
     aws_secret_access_key=app.config['S3_SECRET'],
     config=Config(signature_version='s3v4')
     )
s3_bucket = s3_resource.Bucket(app.config["S3_BUCKET"])

def upload_file_to_s3(response, acl="public-read"):
    try:
        file_data = response.read() 
        content_type = response.getheader('Content-Type')
        file_name = f'{uuid4().hex}.{content_type.split("/")[-1].lower()}'
        s3_bucket.put_object(Key=file_name, Body=file_data, ACL=acl, ContentType=content_type)

    except Exception as e:
        return e

    return "{}{}".format(app.config['S3_LOCATION'], file_name)

def get_bucket_files():
    try:
        images = []
        for file in s3_bucket.objects.all():
            if file.size > 0:
                img_info = {
                'name': file.key,
                'size': file.size,
                'last_modified': file.last_modified
            }
                images.append(img_info)
    except Exception as e:
        return e
    return images