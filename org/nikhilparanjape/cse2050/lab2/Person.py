class Person:
    _firstname = ""
    _lastname = ""

    def __init__(self, firstname, lastname):
        self._firstname = firstname
        self._lastname = lastname

    def to_string(self):
        return "My name is {} {}".format(self._firstname,
                                         self._lastname)


class Student(Person):
    _graduation_year = 0

    def __init__(self, firstname, lastname, graduation_year):
        self._graduation_year = graduation_year
        super(Student, self).__init__(firstname, lastname)

    def to_string(self):
        return "My name is {} {}, I graduate in the year {}".format(self._firstname,
                                                                    self._lastname,
                                                                    self._graduation_year)


kid = Student("John", "Smith", 2025)

print(kid.to_string())
