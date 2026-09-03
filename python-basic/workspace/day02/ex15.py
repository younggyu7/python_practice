#매개변수x, 리턴값x
def hello():
    print("안녕하세요, 여러분.")
    print("만나서 반값습니다!!")

#매개변수o, 리턴값x
def greeting(name):
    print(f"안녕하세요, {name}님")

greeting("피카츄")

#매개변수x, 리턴값o
def getTen():
    print("getTen 실행!")
    return 10

#print(getTen())
result = getTen()
print(result)

#매개변수o, 리턴값o
def mulp(a, b):
    res = a * b
    return res
result = mulp(10, 20)
print(result)

#-----------------------------
#덧셈, 뺄셈, 곱셈, 나눗셈 d이름의 함수
# 각 함수들은 2개의 정수를 입력받아 결과값을 돌려주는 형태

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

def divType(a: int, b: int) -> float:
    return a / b

a = 10
b = 5
print(divType(a, b))