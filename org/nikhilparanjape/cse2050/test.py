from array import *
print("test")

tuple1 = (1, 2, 3, 4, 5, 6)
print(tuple1)
tuple2 = list(tuple1)
print(tuple2)
list2 = tuple(tuple2)
print(list2)

d1 = {"1": "mark", "2": "joe", "3": "smith"}

print(d1.get('2'))


for item in list2:
    print(item)

class CrazyNumber(object):

    def __init__(self,n):
        self.n = n

    def __add__(self, other):
        return self.n - other

    def __sub__(self, other):
        return self.n + other

    def __str__(self):
        return str(self.n)
print(67 * "-")
num = CrazyNumber(10)

print(num)
print(num + 5)
print(num - 20)

print(67 * "-")

array_num = array('i', [1, 3, 5, 7, 9])
for i in array_num:
    print(i)
array_num.append(11)

print(67 * "-")
array_num.reverse()


for i in array_num:
    print(i)