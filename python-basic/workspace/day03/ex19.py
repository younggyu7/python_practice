class Pokemon:
    species = "몬스터"  # 클래스 변수
    name = "hello"

    # 생성자
    def __init__(self, name):
        self.name = name

    # 인스턴스 메서드
    def say_name(self):
        msg = f"내 이름은 {self.name}!"
        print(msg)


pikachu = Pokemon("피카츄")
print(pikachu.name)
kkobugi = Pokemon("꼬부기")
print(kkobugi.name)


# print(Pokemon.species) # 클래스 변수 : 객체 생성 없이 바로 사용 가능


# -------------------------------------------------------------
class Student:
    school = "First Zone"

    def __init__(self, name, score) -> None:
        self.name = name
        self.score = score

    def is_passed(self):
        return self.score >= 60

    def show_info(self):
        result = "합격" if self.is_passed() else "불합격"
        print(f"{self.name}님은 {self.score}점으로 {result}입니다")

    @classmethod
    def show_school(cls):
        print(f"우리는 모두 {cls.school} 학생입니다.")


s1 = Student("라이츄", 75)
s2 = Student("이상해씨", 55)

s1.show_info()
s2.show_info()
Student.show_school()


class Person:
    species = "human"

    def __init__(self, age):
        self._age = age

    # 인스턴스 메서드
    def hello(self):
        print(self._age)

    # 클래스 메서드
    @classmethod
    def show_species(cls):
        print(cls.species)

    # 정적 메서드
    @staticmethod
    def add(a, b):
        return a + b

    # property getter
    @property
    def age(self):
        return (
            self._age
        )  # 단순 age는 무한 반복됨, 은닉 목적, 관례적으로 _한개 붙혀서 사용

    # property setter
    @age.setter
    def age(self, value):
        # 검증하고 값 저장
        if not isinstance(value, int):
            print("저장할 값이 정수가 아닙니다.")
        if value < 0:
            print("나이값은 음수가 불가능합니다.")
        self._age = value  # 단순 age는 무한 반복됨, 은닉 목적


class Item:
    def __init__(self, num):
        self.num = num


item1 = Item(10)
item2 = Item(10)
print(str(Item))
