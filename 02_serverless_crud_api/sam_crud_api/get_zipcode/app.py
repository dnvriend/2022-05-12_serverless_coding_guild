import json
from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute
from pynamodb.exceptions import DoesNotExist

class Blob(Model):
    class Meta:
        table_name = "zipcodes"
        region = 'eu-west-1'
    blob = UnicodeAttribute()
    id = UnicodeAttribute(hash_key=True)

def lambda_handler(event, context):
    try:
        id = event['pathParameters']['code']
        blob = Blob.get(id)
        return {
            "statusCode": 200,
            "body": blob.blob,
        }
    except DoesNotExist:
        return {
            "statusCode": 404,
            "body": f'no zipcode found for: {id}',
        }
