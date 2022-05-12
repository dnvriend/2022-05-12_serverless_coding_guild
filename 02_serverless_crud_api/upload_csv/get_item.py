#!/usr/bin/env python
from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute
from pynamodb.exceptions import DoesNotExist
import json

class Blob(Model):
    class Meta:
        table_name = "zipcodes"
        region = 'eu-west-1'
    blob = UnicodeAttribute()
    id = UnicodeAttribute(hash_key=True)

def get_item():
    try:
        bl = Blob.get('1313HX')
    except DoesNotExist as err:
        print('oops')

if __name__ == '__main__':
    get_item()
