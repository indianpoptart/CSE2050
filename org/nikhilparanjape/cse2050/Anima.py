import random
import sys
import os

class Animal:
    __name = ""
    __height = 0
    __weight = 0
    __sound = 0

    def __init__(self, name, height, weight, sound):
        self.__name = name
        self.__height = height
        self.__weight = weight
        self.__sound = sound

    def set_name(self, name):
        self.name = name

    def get_name(self, ):
        return self.__name
    def get_type(self):
        print(Animal)

    def toString(self):
        return "My name is {}, I am {} lbs, and {} inches tall. I can {} ".format(self.__name,
                                                                                  self.__weight,
                                                                                  self.__height,
                                                                                  self.__sound)


cat = Animal("Kevin", 33, 10, "meow")

print(cat.toString())


class Dog(Animal):
    __owner = ""

    def __init__(self, name, height, weight, sound, owner):
        self.__owner = owner
        super(Dog, self).__init__(name, height, weight, sound)

    def set_owner(self, owner):
        self.__owner = owner


henry = Dog("henry", 56, 65, "bark", "Nikhil")

print(henry.toString())
