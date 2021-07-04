import glom
import json
object_path = json.loads(input("Enter Object Path: "))
key1 = input("Enter key value in format x/y/z: ")
#object_path = {"x":{"y":{"z":"a"}}}
#print(json.loads(object_path))
#key1="x/y"
key1 = key1.replace("/",".")
#print(key1)
actual = glom.glom(object_path, key1, default='path is not correct')
print(actual)


