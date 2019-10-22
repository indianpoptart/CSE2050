class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def push(self, new_data):
        # Allocate the node

    def append(self, new_data):
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while last.next:
            last = last.next

        last.next = new_node

    def printlist(self): # REMEMBER
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def count(self):
        temp = self.head
        count = 0
        while (temp):
            temp = temp.next
            count = count + 1
        return count

