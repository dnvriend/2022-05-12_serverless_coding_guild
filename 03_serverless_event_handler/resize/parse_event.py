#!/usr/bin/env python
import json

with open('example_event.json') as f:
    data = json.load(f)

for record in data['Records']:
    print(record['s3']['bucket']['name'])
    print(record['s3']['object']['key'])
    