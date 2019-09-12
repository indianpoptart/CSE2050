class A:

    def __init__(self):
        print("Initialized A")

    def print(self):
        print("Printing A")


class B(A):
    pass


class C(A):

    def __init__(self):
        super().__init__()
        print("Initialized C")

    def print(self):
        print("Printing C")


class D(B, C):
    pass


zee = D()
zee.print()
