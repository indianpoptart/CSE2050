class ListDeque:
    def __init__(self):
        self._L = []

    def addFirst(self, item):
        self._L.insert(0, item)

    def addLast(self, item):
        self._L.append(item)

    def removeFirst(self):
        return self._L.pop(0)

    def removeLast(self):
        return self._L.pop()

    def __len__(self):
        return len(self._L)

dq = ListDeque()
dq.addFirst(5)
dq.addLast(100)
print(len(dq))
dq.addFirst(1)