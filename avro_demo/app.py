import avro.schema
from avro.datafile import DataFileReader, DataFileWriter
from avro.io import DatumReader, DatumWriter
from pprint import pprint

with open('user.avsc', 'rb') as file:
    schema = avro.schema.parse(file.read())

with DataFileWriter(open("users.avro", "wb"), DatumWriter(), schema) as writer:
    writer.append({"name": "Allen", "favorite_number": 256})
    writer.append({"name": "Ben", "favorite_number": 7, "favorite_color": "red"})

with DataFileReader(open("users.avro", "rb"), DatumReader()) as reader:
    for user in reader:
        pprint(user, indent=4)
