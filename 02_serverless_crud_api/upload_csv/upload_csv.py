#!/usr/bin/env python
from typing import List, Dict
from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute
import json

class Blob(Model):
    class Meta:
        table_name = "zipcodes"
        region = 'eu-west-1'
    blob = UnicodeAttribute()
    id = UnicodeAttribute(hash_key=True)

# The with statement handles opening and closing the file, 
# including if an exception is raised in the inner block. 
# The for line in f treats the file object f as an iterable, 
# which automatically uses buffered I/O and memory management 
# so you don't have to worry about large files.
def read_csv() -> List[map]:
    blobs = []
    with open('postcodes_20190622_4.csv') as f:
        counter = 0
        for line in f:
            if counter == 0:
                counter += 1
            elif counter >= 1 and counter <= 10:
                data = line.split(',')
                blob = parse_line(data)                
                blobs.append(blob)
                counter += 1
            else:
                break
    return blobs

def parse_line(data: List[str]) -> Dict[str, str]:
    return {
        'id': data[0],
        'street': data[1],
        'house_nr': data[2],
        'city': data[3],
        'province': data[7].strip(),
    }

def save_blobs(blobs: List[map]) -> None:
    counter = 0
    with Blob.batch_write() as batch:
        for blob in blobs:
            data = Blob(id=blob['id'], blob=json.dumps(blob))
            print(json.dumps(blob))
            batch.save(data)
            counter += 1
            print(f'saving: {counter}/{len(blobs)}')


if __name__ == '__main__':
    blobs = read_csv()
    save_blobs(blobs)
    print('done uploading csv')