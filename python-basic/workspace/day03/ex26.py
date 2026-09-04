class Person:
    def __init__(self):
        self.age = 0

    def set_age(self, v):
        if not isinstance(v, int):
            raise TypeError("입력하신 데이터 타입이 맞이 않아요..")  # 강제 에외 발생
        if v < 0:
            raise ValueError("나이는 음수가 될숭 없습니다.")  # 강제 에외 발생
        self.age = v


# p = Person()
# print(p.age)
# try:
#     p.set_age("asb")
# except TypeError as e:
#     print("예외 발생 : ", e)
#     raise  # 원래 예외를 그대로 다시 발생시키기
# except ValueError as e:
#     print("예외 발생 : ", e)
# else:
#     print(p.age)


# ---------------------------
class MyException(Exception):
    pass


try:
    print("내가 만든 예외를 발생시켜보자~~")
    raise MyException("예외 발생! 경고 경고!")
except MyException as e:
    print("예외를 처리하자 : ", e)
