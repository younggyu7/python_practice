from abc import ABC, abstractmethod


# 추상클래스
class Animal(ABC):
    # 추상메서드
    @abstractmethod
    def sound(self):
        pass


class Cat(Animal):
    def sound(self):
        print("야옹~~~")


class Dog(Animal):
    def sound(self):
        print("멍멍!!")


dog = Dog()
dog.sound()

cat = Cat()
cat.sound()
