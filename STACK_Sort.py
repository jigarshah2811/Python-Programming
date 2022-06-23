from STACK import Stack


def sort_stack(src):
    result = Stack()

    while not src.isEmpty():
        item = src.pop()
        while not result.isEmpty() and item > result.peek():
            src.push(result.pop())
        result.push(item)
    return result


def main():
    source = Stack()

    vals = [1, 3, 2, 5, 7, 100, 30, 12, 4]

    for val in vals:
        source.push(val)

    result = sort_stack(source)
    for i in xrange(result.size()):
        print result.pop()

if __name__ == "__main__":
    main()
