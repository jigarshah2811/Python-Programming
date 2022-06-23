from STACK import Stack


def sort_stack(srcStack):
    destStack = Stack()

    while not srcStack.isEmpty():
        item = srcStack.pop()

        # Check if the item is bigger then what's on destStack - then it has to be sorted (placed on src temporary)
        while not destStack.isEmpty() and item > destStack.peek():
            srcStack.push(destStack.pop())
        destStack.push(item)
    return destStack


def main():
    source = Stack()

    vals = [1, 3, 2, 5, 7, 100, 30, 12, 4]

    for val in vals:
        source.push(val)

    destStack = sort_stack(source)
    for i in range(destStack.size()):
        print(destStack.pop())

if __name__ == "__main__":
    main()
