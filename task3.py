import glom
import json
import sys

try:
	object_path = json.loads(input("Enter Object Path: "))
except json.decoder.JSONDecodeError:
    print("Object path or format  is not correct")
    sys.exit(1)

key1 = input("Enter key value in format x/y/z: ")
key1 = key1.replace("/",".")

key_value = glom.glom(object_path, key1, default='path is not correct')
print(key_value)
