import json

data = '{"name":"Vaibhav","age":22}'

obj = json.loads(data)

print(obj["name"])
