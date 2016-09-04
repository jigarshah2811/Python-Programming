from STACK import Stack


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if len(self.items):
            return self.items.pop()

    def size(self):
        return len(self.items)

    def print_queue(self):
        print self.items


class QueueFrom2Stacks():
    def __init__(self):
        self.src = Stack()
        self.dest = Stack()

    def enqueue(self, item):
        if self.src.isEmpty():
            self.src.push(item)
        else:
            self.dest.push(item)

    def dequeue(self):
        while not self.src.isEmpty():
            self.dest.push(self.src.pop())
        try:
            self.dest.pop()
        except IndexError:
            print "Queue is Empty"

    def isEmpty(self):
        return self.src.isEmpty() and self.dest.isEmpty()

    def size(self):
        return self.src.size() + self.dest.size()

    def print_queue(self):
        print self.src.items
        print self.dest.items

"""
Testing for Module
"""

"""
def main():
    # q = QueueFrom2Stacks()
    q = Queue()
    # Expecting Empty message
    q.dequeue()

    # Expecting 10, 20, 30
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    q.dequeue()
    q.print_queue()
    # Removed 10, expecting 20, 30

    q.dequeue()
    q.print_queue()

    q.dequeue()
    q.print_queue()

    q.enqueue(40)
    q.enqueue(50)
    q.enqueue(60)
    q.dequeue()
    q.enqueue(70)
    q.enqueue(80)
    q.enqueue(90)
    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.dequeue()

    q.print_queue()


if __name__ == "__main__":
    main()

"""