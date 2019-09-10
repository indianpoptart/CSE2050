class ListStack:
    def __init__(self):
        self._L = []

    def push(self, item):
        self._L.append(item)

    def pop(self):
        return self._L.pop()

    def peek(self):
        return self._L(len(self._L)-1)

    def __len__(self):
        return len(self._L)

    def isempty(self):
        return len(self) == 0

stack1 = ListStack()
print(stack1.push(5))
print(stack1)
stack1.push(3)
print(len(stack1))