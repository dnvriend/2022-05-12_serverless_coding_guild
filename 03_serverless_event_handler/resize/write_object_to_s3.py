#!/usr/bin/env python
import boto3

s3 = boto3.client('s3')
with open("cat_from_s3.jpg", "rb") as f:
    s3.upload_fileobj(f, "serverless-event-handler-dstbucket-xaaz1rizim8o", "cat_from_s3.jpg")
