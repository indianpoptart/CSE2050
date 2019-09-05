class Vector(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def norm(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5


num = Vector(123, 4512)
n1 = float(input("Give me a value for x: "))
n2 = float(input("Give me a value for y: "))
customnum = Vector(n1, n2)
print('sqrt({}^2 + {}^2) = {}'.format(n1, n2, customnum.norm()))

