#!/usr/bin/env python
from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute
import json

class Blob(Model):
    class Meta:
        table_name = "zipcodes"
        region = 'eu-west-1'
    blob = UnicodeAttribute()
    id = UnicodeAttribute(hash_key=True)

def scan_table():
    for item in Blob.scan():
        print(item.blob)

def scan_table_as_list():
    xs = list(Blob.scan())
    ys = list(map(lambda x: json.loads(x.blob), xs))
    print(json.dumps(ys))

if __name__ == '__main__':
    scan_table_as_list()