from QUEUE import Queue


class Stack:

    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, item):
        while not self.q1.isEmpty():
            self.q2.enqueue(self.q1.dequeue())
        self.q1.enqueue(item)
        while not self.q2.isEmpty():
            self.q1.enqueue(self.q2.dequeue())

    def pop(self):
        self.q1.dequeue()

    def size(self):
        return self.q1.size() + self.q2.size()

    def printStack(self):
        print self.q1.items


def main():
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    print s.printStack()
    s.pop()
    print s.printStack()

    s.push(4)
    s.push(5)
    s.pop()
    print s.printStack()


if __name__ == "__main__":
    main()
