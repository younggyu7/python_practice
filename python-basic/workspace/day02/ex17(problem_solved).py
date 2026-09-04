# 문제1. 요소 5개의 리스트를 하나 만들어서, 인덱스 번호 두개를 입력받고,
#       해당 인덱스 번호에 자리한 값을 교환해 보세요.
# 힌트 : 입력받기 -> 변수 = input("콘솔에 출력할 메세지")
#       input으로 입력받은 값은 무조건 str 타입으로 가져온다.

# 문제2. [1,3,4,5,2] 값을 갖는 리스트를 만들고, [5,4,3,2,1] 로 만들어 보세요.

# 문제3. lst = ["korea", ["IT", [1,3,5,7,9], ["even", [0,2,4,6,8]]]]
#       위 lst 리스트에서 Korea 출력
#       숫자 3 출력
#       숫자 8 출력

# 문제4. 국어,영어,수학 3과목에 대한 점수를 입력받아 총점, 평균을 구하여 출력해보세요.

"""문제5. 카페 주문 프로그램
메뉴를 출력하고, 주문은 메뉴 번호로 계속 받습니다.
종료를 선택하면 주문이 종료되고, 주문한 메뉴들의 총 합을 출력합니다.
메뉴
*** 퍼스트존 카페 ***
1. 아메리카노: 2000원
2. 카페라떼: 3000원
3. 화이트모카라떼: 4000원
4. 자바칩프라푸치노: 4500원
5. 종료
"""

""" 문제6. Up, Down 게임 
    1 ~ 100사이 임의의 숫자를 입력받고, 그 숫자를 맞추는 게임 
    추측한 숫자가 임의의 숫자보다 크면 "Down", 작으면 "Up" 출력, 
    임의의 숫자를 맞추면 "축하합니다! 맞췄습니다." 출력 후 게임 종료되며, 
    게임을 다시 할 것인지 y또는n으로 입력받는다. 
    y를 입력하면 다시 게임이 시작하며, n을 입력하면 게임이 완전히 종료된다. 
    콘솔 예시 :
    게임 시작! 숫자를 맞춰 주세요~ 
    1~100
    1>>  30 (사용자가 숫자 입력)
    "Up"

    30~100
    2>>  40 
    "Up"

    40~100
    3>>  80
    "Down"

    40~80
    4>>  65
    "맞췄습니다. 축하합니다!!" 
    게임을 다시 시작하시겠습니까?(y/n)  y 

    게임 시작! 숫자를 맞춰 주세요~ 
    1~100
    1>>   
    ....
    게임을 다시 시작하시겠습니까?(y/n)  n 
    게임 종료!! 
"""

print("=" * 5, "문제1", "=" * 5)
list = ["apple", "banana", "graph", "watermelon", "cherry"]
while True:
    text = input("인덱스 번호 2개를 입력하세요 : ")
    value = text.split()
    if not len(value) == 2:
        print("번호를 2개를 입력하세요")
        continue
    if not value[0].isdigit() or not value[1].isdigit():
        print("숫자를 입력해주세요")
        continue
    a = int(value[0])
    b = int(value[1])

    if a > 4 or a < 0 or b > 4 or b < 0:
        print("0에서 4 사이의 숫자를 입력해주세요")
        continue
    break


print(list[a], " : ", list[b])
print("=" * 13)


print("=" * 5, "문제2", "=" * 5)
list = [1, 3, 4, 5, 2]
list.sort(reverse=True)
print(list)
print("=" * 13)


print("=" * 5, "문제3", "=" * 5)
lst = ["korea", ["IT", [1, 3, 5, 7, 9], ["even", [0, 2, 4, 6, 8]]]]
print(lst[0])
print(lst[1][1][1])
print(lst[1][2][1][4])
print("=" * 13)


print("=" * 5, "문제4", "=" * 5)
sum = 0
avg = 0
korean = input("korean score : ")
if not korean.isdigit():
    korean = input("retype korean score : ")
sum += int(korean)

english = input("english score : ")
if not english.isdigit():
    korean = input("retype english score : ")
sum += int(english)

math = input("math score : ")
if not math.isdigit():
    math = input("retype maht score : ")
sum += int(math)
avg = sum / 3
print("sum : ", sum, ", ", "avg : ", avg)
print("=" * 13)


print("=" * 5, "문제5", "=" * 5)
print(
    "메뉴\n",
    "*** 퍼스트존 카페 ***\n",
    "1. 아메리카노: 2000원\n",
    "2. 카페라떼: 3000원\n",
    "3. 화이트모카라떼: 4000원\n",
    "4. 자바칩프라푸치노: 4500원\n",
    "5. 종료\n",
)
sum = 0
menu = {"1": 2000, "2": 3000, "3": 4000, "4": 4500}


def menu_choice():
    total = 0
    while True:
        choice = input("주문할 메뉴 번호를 입력하세요 : ")
        if not choice.isdigit():
            print("메뉴 번호를 입력해주세요")
            continue
        if int(choice) > 5 or int(choice) < 0:
            print("1에서 4번 사이의 메뉴 숫자를 눌러주세요")
            continue
        if choice == "5":
            break
        total += menu[choice]
    return total


sum = menu_choice()
if sum == 0:
    print("주문한 내역이 없습니다")
    choice = input("다시주문하시겠습니까? (y/n)")
    if choice == "y":
        sum = menu_choice()
        print("총 : ", sum, "원 입니다.")
    else:
        print("주문 내역이 없이 종료됩니다.")
else:
    print("총 : ", sum, "원 입니다.")
print("=" * 13)


import random

print("=" * 5, "문제6", "=" * 5)


def find_number():
    answer = random.randint(1, 100)
    while True:
        n = input("choose a number from 1 to 100 : ")
        if not n.isdigit():
            n = input("input is not a number\n choose a number from 1 to 100 again: ")
        n = int(n)
        if n > 100 or n < 0:
            n = int(input("wrong number!, choose a number from 1 to 100 : "))

        if n > answer:
            print("Down")
        elif n < answer:
            print("Up")
        else:
            print("맞췄습니다. 축하합니다!!")
            restart = input("게임을 다시 시작하시겠습니까?(y/n)")
            if restart == "y":
                find_number()
            else:
                break


find_number()
print("=" * 13)
