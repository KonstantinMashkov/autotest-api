import json

# json_data = """
# {"name": "ivan", "age": 30, "spisok": ["sdfsdf","dgdfgdf"]}
# """
# parsed_data = json.loads(json_data)
# print(parsed_data)

# data = {
#     "name": "ivan", 
#     "age": 30
#     }

# json_str = json.dumps(data)
# print(json_str)

with open("json_example.json", "r", encoding="utf-8") as file:
    data = json.load(file)
    print(data)
    
with open("json_user.json", "w", encoding="utf-8") as file:
    json.dump(data, file, indent=2, ensure_ascii=False)
    