# 예외 처리
lst = [1, 2, 3]
try:
    num = int(input("정수 : "))
    print(num)
    print(3 / num)
    print(lst[num])
# except ValueError:
#     print("숫자를 잘 입력해주세요....")
# except ZeroDivisionError:
#     print("0으로 나눌 수 없습니다.")
except IndexError:
    print("인덱스 번호를 잘 못 입력하셨습니다.")
except Exception as e:
    print("예외가 발생합습니다..", e)
else:
    print("예외 없이 실행됨")
finally:
    print("항상 실행되는 코드블럭")
