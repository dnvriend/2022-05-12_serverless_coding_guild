import json
from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute

class Blob(Model):
    class Meta:
        table_name = "zipcodes"
        region = 'eu-west-1'
    blob = UnicodeAttribute()
    id = UnicodeAttribute(hash_key=True)

def lambda_handler(event, context):
    xs = list(Blob.scan())
    ys = list(map(lambda x: json.loads(x.blob), xs))    
    return {
        "statusCode": 200,
        "body": json.dumps(ys),
    }
