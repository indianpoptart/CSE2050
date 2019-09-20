class Queue:
    def __init__(self):
        self._head = 0
        self._L = []

    def enqueue(self, item):
        self._L.append(item)

    def dequeue(self):
        item = self._L[self._head]
        self._head += 1
        return item

    def __len__(self):
        return len(self._L) - self._head

    def isempty(self):
        return len(self) == 0


queue1 = Queue()
queue1.enqueue(5)
print(len(queue1))
queue1.enqueue(100)
queue1.enqueue(200)

print(len(queue1))