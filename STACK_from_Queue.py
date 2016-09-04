from QUEUE import Queue


class Stack:

    def __init__(self):
        self.q = Queue()

    def push(self, val):
        self.q.enqueue(val)
        for i in xrange(self.q.size()):
            self.q.enqueue(self.q.dequeue())

    def pop(self):
        return self.q.dequeue()

    def size(self):
        return self.q.size()


def main():
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    print s.pop()


if __name__ == "__main__":
    main()
