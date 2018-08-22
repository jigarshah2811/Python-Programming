from STACK import Stack
class Queue:
    def __init__(self, size=100):
        self.items = []
        self.maxSize = size

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return len(self.items) == 0

    def isFull(self):
        return len(self.items) >= self.maxSize

    def enqueue(self, item):
        if not self.isFull():
            self.items.insert(0, item)
        else:
            return -1
            # raise Exception("Queue is Full")

    def dequeue(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            return -1
            # raise Exception("Queue is Empty")

    def print_queue(self):
        print self.items


class QueueFromStacks(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s1 = Stack()
        self.s2 = Stack()


    def enqueue(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.s1.push(x)

    def dequeue(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if self.isEmpty():
            return -1
        if not self.s2.isEmpty():
            ele = self.s2.peek()
            self.s2.pop()
            return ele
        while not self.s1.isEmpty():
            self.s2.push(self.s1.pop())
        ele = self.s2.peek()
        self.s2.pop()
        return ele

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if not self.s2.isEmpty():
            return self.s2.peek()
        while not self.s1.isEmpty():
            self.s2.push(self.s1.pop())
        return self.s2.peek()

    def isEmpty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return self.s1.isEmpty() and self.s2.isEmpty()

"""
Testing for Module
"""

def main():
    # q = QueueFromStacks()
    q = Queue()
    # Expecting Empty message
    q.dequeue()


    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    # q.print_queue()

    print q.dequeue() # Should return [1]
    # q.print_queue()

    q.enqueue(4)
    q.enqueue(5)
    q.enqueue(6)
    print q.dequeue() # Should return  2
    print q.dequeue()  # Should return 3
    q.enqueue(7)
    q.enqueue(8)
    q.enqueue(9)
    print q.dequeue() # should return everythign after 4, 5, 6, 7. 8 , 9
    print q.dequeue()
    print q.dequeue()
    print q.dequeue()
    print q.dequeue()
    print q.dequeue()
    print q.dequeue()

    # q.print_queue()


if __name__ == "__main__":
    main()

