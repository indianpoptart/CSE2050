import heapq

# Nikhil Paranjape
# CSE 2050
# Ocrober 11 2019


class PriorityQueue(object):
    def __init__(self):
        self.queue = []

    def __str__(self):
        return ' '.join([str(i) for i in self.queue])

    def is_empty(self):
        return len(self.queue) == []

    def insert(self, data):
        self.queue.append(data)

    def delete(self):
        try:
            temp = 0
            for i in range(len(self.queue)):
                if self.queue[i] > self.queue[temp]:
                    temp = i
            item = self.queue[temp]
            del self.queue[temp]
            return item
        except IndexError:
            print()
            exit()


class Heap(object):
    def __init__(self):
        self.heap = []


if __name__ == '__main__':
    print("Question 1:")
    question1 = PriorityQueue()
    question1.insert(4)
    question1.insert(5)
    question1.insert(6)
    question1.insert(15)
    question1.insert(9)
    question1.insert(7)
    question1.insert(20)
    question1.insert(16)
    question1.insert(25)
    question1.insert(14)
    question1.insert(12)
    question1.insert(11)
    question1.insert(13)
    print("1A.", question1)
    print("1B. The Min element in the Priority Queue is :", question1.delete())

    print()
    print("Question 2:")
    question2 = [1, 5, 8, 11, 6, 10, 14, 13, 8, 9, 12, 15, 14, 16, 8, 18]
    heapq.heapify(question2)
    print("2A. The min-heap is :", question2)
    print("2B. The max heap of the array is : ", heapq.heappop(question2))
    print("2C. The 3 biggest numbers in list are : ", heapq.nlargest(3, question2))
