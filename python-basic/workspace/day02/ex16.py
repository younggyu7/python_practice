# 매개변수 기본값 지정 : 인자 생략하면 default(기본)값으로 처리
def greeting(age, name="아무개"):
    print(f"안녕하세요, {age}살의 {name}님")


# 키워드 인자 : 순서 변경 가능
def info(name, age):
    print(f"{name}님의 나이는 {age}세입니다.")


info(age = 20, name = "피카츄")

# 가변 인자 : 여러 인자들을 하나의 매개변수에 담아주는 역할
def total (num, age = 1000, *args):
    print(num, age, args)
    print(type(args))
    return sum(args)

print(total(10, 20, 30, 40, 50))

# 여러 개의 키 = 값 인자
def show_info(**kwargs):
    print(type(kwargs))
    for key, value in kwargs.items():
        print(f"{key} : {value}" )


show_info(name= "Tom", age = 20)
show_info(name="Tom", age = 20, email= "test@test.com")

#리턴값 여러개 -> tuple로 리턴
def get_name_and_age():
    return "Anne", 35

name , age = get_name_and_age()
print(type(get_name_and_age()))
print(type(name))
print(type(age))
print(name)
print(age)

# 함수 구현부 생략 ... 혹은 pass
def test():
    pass

def test2():
    ...

def greet():
	print("hello")
	
def exec(func): # 함수를 매개변수로 받고 
	func()        # 매개변수로 호출가능 
	
exec(greet)  # 함수를 인자로 전달 
