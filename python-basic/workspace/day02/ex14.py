fruits: list[str] = ["apple", "banana", "cherry"]
print(fruits[0])

colors: tuple[str, str, str] = 'red', 'green', 'blue'
print(colors[0])

person: dict[str, object] = {
    'name':'pika',
    'age':10,
    'is_stu':True
}
print(person['name'])

numbers: set[int] = {1, 2, 2, 3, 4}
print(numbers)