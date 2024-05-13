import json
user ={
    "id" : "gildong",
    "password" : "192837",
    "age" : 30,
    "hobby" : ["football", "programming"]

}

# 인코딩
json_data = json.dumps(user, indent=4)
print(json_data)

# 디코딩
data = json.loads(json_data)
print(data)

# 파일로 저장
with open("C:/algorithm_practice/develop_test/user.json", "w", encoding = "utf-8")as file:
    json.dump(user, file, indent = 4)