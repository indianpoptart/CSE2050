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
        pass

    def get_name(self):
        return self.__name

    def get_type(self):
        print(Animal)

    def get_sound(self):
        return self.__sound

    def to_string(self):
        return "My name is {}, I am {} lbs, and {} inches tall. I can {} ".format(self.__name,
                                                                                  self.__weight,
                                                                                  self.__height,
                                                                                  self.__sound)


cat = Animal("Kevin", 33, 10, "meow")


class Dog(Animal):
    __owner = ""

    def __init__(self, name, height, weight, sound, owner):
        self.__owner = owner
        super(Dog, self).__init__(name, height, weight, sound)

    def set_owner(self, owner):
        self.__owner = owner

    def get_owner(self):
        return self.__owner


henry = Dog("Henry", 56, 65, "bark", "Nikhil")

print("My name is {}. I can {}! My owner's name is {}".format(henry.get_name(),
                                                                henry.get_sound(),
                                                                henry.get_owner()))

