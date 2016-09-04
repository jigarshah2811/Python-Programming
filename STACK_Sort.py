from STACK import Stack

def sortStack(source):
    dest = Stack()
    while not source.isEmpty():
        ele = source.pop()
        while not dest.isEmpty() and ele < dest.peek():
            source.push(dest.pop())
        dest.push(ele)
    return dest


def main():
    source = Stack()

    vals = [1, 3, 2, 5, 7, 100, 30, 12, 4]

    for val in vals:
        source.push(val)

    dest = sortStack(source)
    for i in range(dest.size()):
        print dest.pop()

if __name__ == "__main__":
    main()
