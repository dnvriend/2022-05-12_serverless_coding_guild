from PIL import Image
import boto3
import os

def get_file_name(object_key: str) -> str:
    return object_key.split('.')[0]

def get_file_extension(object_key: str) -> str:
    return object_key.split('.')[1]

def get_thumbnail_filename(object_key: str) -> str:
    return f'{get_file_name(object_key)}_thumbnail.{get_file_extension(object_key)}'

def thumbnail_image(object_key: str) -> None:
    image = Image.open(f'/tmp/{object_key}')
    image.thumbnail((400, 400))
    image.save(f'/tmp/{get_thumbnail_filename(object_key)}')

def get_bucket_name(event: map) -> str:
    record = event['Records'][0]
    return record['s3']['bucket']['name']

def get_object_key(event: map) -> str:
    record = event['Records'][0]
    return record['s3']['object']['key']

def write_object_to_tmp(bucket_name: str, object_key: str) -> None:
    print(f'write_object_to_tmp({bucket_name}, {object_key})')
    s3 = boto3.client('s3')
    with open(f'/tmp/{object_key}', 'wb') as f:
        s3.download_fileobj(bucket_name, object_key, f)

def write_thumbnail_to_dst(dst_bucket_name: str, object_key: str) -> None:
    print(f'write_thumbnail_to_dst({dst_bucket_name}, {object_key})')
    s3 = boto3.client('s3')
    with open(f'/tmp/{get_thumbnail_filename(object_key)}', "rb") as f:
        s3.upload_fileobj(f, dst_bucket_name, get_thumbnail_filename(object_key))

def lambda_handler(event, context):
    dst_bucket_name = os.environ['DST_BUCKET_NAME']
    object_key = get_object_key(event)
    bucket_name = get_bucket_name(event)
    print(f'''
dst_bucket_name: {dst_bucket_name}
object_key = {object_key}
bucket_name = {bucket_name}
thumbnail_filename = {get_thumbnail_filename(object_key)}''')
    write_object_to_tmp(bucket_name, object_key)
    thumbnail_image(object_key)
    write_thumbnail_to_dst(dst_bucket_name, object_key)
