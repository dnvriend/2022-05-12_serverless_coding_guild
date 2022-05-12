#!/usr/bin/env python
import boto3

s3 = boto3.client('s3')
with open('cat_from_s3.jpg', 'wb') as f:
    s3.download_fileobj('serverless-event-handler-srcbucket-ewv3o2wa5iek', 'cat.jpg', f)
