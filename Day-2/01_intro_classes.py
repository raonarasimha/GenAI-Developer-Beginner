# 1. Define a class using class keyword
class Dog:
    def __init__(self, name, age):
        self.name = name  # instance attribute
        self.age = age

    def bark(self):
        print(f"{self.name} says: Woof!")

if __name__ == "__main__":
    dog1 = Dog("Buddy", 3)
    dog2 = Dog("Lucy", 5)

    dog1.bark()
    dog2.bark()
    print(f"{dog1.name} is {dog1.age} years old.") 