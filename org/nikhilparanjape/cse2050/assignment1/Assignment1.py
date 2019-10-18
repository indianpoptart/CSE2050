# Nikhil Paranjape
# CSE 2050
# September 24, 2019


# Question 1
class ListNode:
    def __init__(self, dat, prev=None, link=None):
        self.dat = dat
        self.prev = prev
        self.link = link

        if prev is not None:
            self.prev.link = self
        if link is not None:
            self.link.prev = self

    def display(self):
        node = self
        while node:
            print(node.dat, '', end='')
            node = node.link

    def disp_rec(self):
        print(self.dat, '', end='')
        if self.link:
            self.link.disp_rec()

    def length(self):
        if self.link is None:
            return 1
        return 1 + self.link.length()

    def reverse(self, new_list=None):
        if self.link is None:
            return ListNode(self.dat, new_list)
        return self.link.reverse(ListNode(self.dat, new_list))

    def reverse2(self):
        lst = self
        new_list = None
        while lst:
            lst.link, lst, new_list = new_list, lst.list, lst
        return new_list


# Question 2
class LinkedList:
    def __init__(self):
        self._head = None

    def addfirst(self, item):
        self._head = ListNode(item, self._head)

    def addlast(self, item):
        if self._head is None:
            self.addfirst(item)
        else:
            currnode = self._head
            while currnode.link is not None:
                currnode = currnode.link
            currnode.link = ListNode(item)

    def removefirst(self):
        item = self._head.data
        self._head = self._head.link
        return item

    def removelast(self):
        if self._head.link is None:
            return self.removefirst()
        else:
            currnode = self._head
            while currnode.link.link is not None:
                currnode = currnode.link
            currnode.link = None
            return currnode.dat

    def length(self):
        pass


# Question 3
class DoublyLinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._length = 0

    def __len__(self):
        return self._length

    def __iadd__(self, other):  # overrides += operator
        if other._head is None:
            return
        if self._head is None:
            self._head = other._head
        else:
            self._tail.link = other._head
            other._head.prev = self._tail
        self._tail = other._tail
        self._length = self._length + other._length

        other.__init__()
        return self

    def _addbetween(self, item, before, after):
        node = ListNode(item, before, after)
        if after is self._head:
            self._head = node
        if before is self._tail:
            self._tail = node
        self._length += 1

    def addfirst(self, item):
        self._addbetween(item, None, self._head)

    def addlast(self, item):
        self._addbetween(item, self._tail, None)

    def _remove(self, node):
        before, after = node.prev, node.link
        if node is self._head:
            self._head = after
        else:
            before.link = after
        if node is self._tail:
            self._tail = before
        else:
            after.prev = before
        self._length -= 1
        return node.data

    def removefirst(self):
        return self._remove(self._head)

    def removelast(self):
        return self._remove(self._tail)


# Question 4
class ListQueue:
    def __init__(self):
        self._L = []

    def enqueue(self, item):
        self._L.append(item)

    def dequeue(self):
        return self._L.pop(0)

    def __len__(self):
        return len(self._L)

    def isempty(self):
        return len(self._L) == 0


# Question 5
class LinkedListStack:
    def __init__(self):
        self._L = LinkedList()

    def push(self, item):
        self._L.addfirst(item)

    def pop(self):
        return self._L.removefirst()

    def __len__(self):
        return self._L.length()


print("Question 1")
ln1 = ListNode("1,2,3,4,5,6")
print("a. ")
print(ln1.disp_rec())
ln1.reverse()
print("b. ")
print(ln1.display())
print(ln1)
