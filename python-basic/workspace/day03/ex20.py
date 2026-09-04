class Person:
    test = "test"

    def __init__(self, name):
        self.name = name

    def work(self):
        print(f"{self.name}이/가 일을 한다.")


class Postman(Person):  # self.name, work()
    # 오버라이딩 "부모로부터 물려받은 기능이 마음에 안들어, 내용물을 수정하는 것"
    # 부모 클래스의 생성자를 받지 못한다
    def __init__(self, name, postman_id):
        super().__init__(name)  # 부모 생성자 호출하여 name 속성 초기화
        self.postman_id = postman_id

    def work(self):
        print(f"{self.name}이/가 우편물을 배달한다.")


p = Postman("우체부", 101)
print(p.name)  # 부모클래스 인스턴스 변수
print(p.postman_id)  # 자식 클래스의 인스턴스 변수


# class A:
#     def __init__(self):
#         print("A 생성자")

#     def aaa(self):
#         pass


# class B:
#     def __init__(self):
#         print("B 생성자")

#     def bbb(self):
#         pass


# class C:
#     def __init__(self):
#         print("C 생성자")

#     def ccc(self):
#         pass


# class D(A, B, C):
#     def __init__(self):
#         print("D 생성자")


# a = A()
# d = D()


# ---------------------
class A:
    def hello(self):
        print("hello AAA")


class B(A):
    # override
    def hello(self):
        print("hello BBB")


class C(A):
    # override
    def hello(self):
        print("hello CCC")


class D(B, C):
    # override
    def hello(self):
        print("hello DDD")
        super().hello()
        super(D, self).hello()  # BBB
        super(C, self).hello()  # AAA
        super(B, self).hello()  # CCC
        # super(A, self).hello() # object는 hello() 메서드 없음


x = D()
x.hello()
