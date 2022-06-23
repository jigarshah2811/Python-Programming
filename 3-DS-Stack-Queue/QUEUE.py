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
        print(self.items)


class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.k = k
        self.q = ['#'] * k
        self.front = 0
        self.rear = 0
        self.empty = True

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the empty queue. Return true if the operation is successful.
        """
        q, k, front, rear, empty = self.q, self.k, self.front, self.rear, self.empty

        if self.isFull():
            return False

        if front == rear and self.empty:    # if the queue is full now, front will match rear
            empty = False

        q[rear] = value
        rear = (rear + 1) % k

        self.rear, self.empty = rear, empty
        return True

    def deQueue(self) -> bool:
        """
        Delete an element from the empty queue. Return true if the operation is successful.
        """
        q, k, front, rear, empty = self.q, self.k, self.front, self.rear, self.empty

        if self.isEmpty():
            return False

        front = (front + 1) % k
        if front == rear and not empty:     # If the queue is empty now, rear will match front
            empty = True

        self.front, self.empty = front, empty
        return True

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        q, k, front, rear, empty = self.q, self.k, self.front, self.rear, self.empty
        if self.isEmpty():
            return -1
        return q[front]

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        q, k, front, rear, empty = self.q, self.k, self.front, self.rear, self.empty
        if self.isEmpty():
            return -1
        return q[rear]

    def isEmpty(self) -> bool:
        """
        Checks whether the empty queue is empty or not.
        """
        q, k, front, rear, empty = self.q, self.k, self.front, self.rear, self.empty

        if front == rear and empty:
            return True

        return False

    def isFull(self) -> bool:
        """
        Checks whether the empty queue is full or not.
        """
        q, k, front, rear, empty = self.q, self.k, self.front, self.rear, self.empty

        if front == rear and not empty:
            return True

        return False




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
def testQueueFromStack():
    # q = QueueFromStacks()
    q = Queue()
    # Expecting Empty message
    q.dequeue()


    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    # q.print_queue()

    print(q.dequeue()) # Should return [1]
    # q.print_queue()

    q.enqueue(4)
    q.enqueue(5)
    q.enqueue(6)
    print(q.dequeue()) # Should return  2
    print(q.dequeue())  # Should return 3
    q.enqueue(7)
    q.enqueue(8)
    q.enqueue(9)
    print(q.dequeue()) # should return everythign after 4, 5, 6, 7. 8 , 9
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())

    # q.print_queue()

def testCircularQueue():

    #Your MyCircularQueue object will be instantiated and called as such:
    obj = MyCircularQueue()
    param_1 = obj.enQueue(1)
    param_1 = obj.enQueue(2)
    param_1 = obj.enQueue(3)
    param_1 = obj.enQueue(4)
    param_2 = obj.deQueue()
    param_3 = obj.Front()
    param_4 = obj.Rear()
    param_5 = obj.isEmpty()
    param_6 = obj.isFull()

def main():
    #testQueueFromStack()
    testCircularQueue()

if __name__ == "__main__":
    main()

