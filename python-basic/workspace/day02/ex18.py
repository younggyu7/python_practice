# 클래스 정의
class Person:
    # 클래스 변수
    nation = "Korea"

    # 생성자
    def __init__(self):
        print("생성자 호출!")
        # 인스턴스 변수
        self.name = ""
        self.age = 0
        # 지역변수
        x = 10


# 함수
def hello():
    # 지역변수
    y = 20


# 전역변수
abc = 10


# 객체 생성 : p1,p2 등은 참조변수
p1 = Person()
p2 = Person()
p3 = Person()

print(Person.nation)
print(p1.nation)
print(p2.nation)
print(p3.nation)
print("-----------")
# Person.nation = "US"
p1.nation = "UK"  # 인스턴스 변수화
print(Person.nation)
print(p1.nation)
print(p2.nation)
print(p3.nation)


"""
print("p1.name : ", p1.name)
print("p1.age : ", p1.age)
p1.name = "피카츄"
p1.age = 10
print("p1.name : ", p1.name)
print("p1.age : ", p1.age)
print("p2.name : ", p2.name)
print("p2.age : ", p2.age)
"""
