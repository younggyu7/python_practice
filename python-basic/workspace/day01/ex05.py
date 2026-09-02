# dict

person = {"name": "pikachu", "age": 10, "height": 230.5}
print(person)

# 키로 값 조회
print(person["name"])
print(person.get("name"))

person["email"] = "pika@gmail.com"
print(person)
del person["email"]
print(person)
print(person.keys())
t = list(person.values())
print(t)
