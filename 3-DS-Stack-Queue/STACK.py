class Stack:
    def __init__(self, size=100):
        self.items = []
        self.maxSize = size

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return len(self.items) == 0

    def isFull(self):
        return len(self.items) > self.maxSize

    def push(self, new_item):
        self.items.append(new_item)

    def peek(self):
        return self.items[len(self.items)-1]   # Last item in the list

    def pop(self):
        item = self.items.pop()     # pop() == LIFO removes the last item from list and returns value
        return item                 # pop(0) == FIFO !


class StackWithMin(Stack):
    INT_MAX = 65535

    def __init__(self, size=100):
        Stack.__init__(self, size)
        self.stack = Stack(size)
        self.min_stack = Stack(size)
        self.min_stack.push(self.INT_MAX)

    def push(self, new_item):
        if new_item < self.min_stack.peek():
            self.min_stack.push(new_item)
        self.stack.push(new_item)

    def pop(self):
        item = self.stack.pop()
        if item <= self.min_stack.peek():
            self.min_stack.pop()

    def min(self):
        return self.min_stack.peek()


class SetOfStack(Stack):

    def __init__(self, num_stacks=3, size=100):
        Stack.__init__(self, size)
        self.num_stacks = num_stacks
        self.s = [Stack(self.maxSize) for count in range(self.num_stacks)]

    def size(self):
        sum = 0
        for stack_num in range(self.num_stacks):
            sum += self.s[stack_num].size()
        return sum

    def isEmpty(self):
        return len(self.s) == 0

    def isFull(self):
        return len(self.s) > self.num_stacks * self.maxSize

    def push(self, item, stack_to_operate=0):
        for stack_num in range(self.num_stacks):
            if stack_num == stack_to_operate:
                self.s[stack_num].push(item)

    def pop(self, stack_to_operate=0):
        for stack_num in range(self.num_stacks):
            if stack_num == stack_to_operate:
                return self.s[stack_num].pop()


def main():
    num_of_stacks = 3
    stack_size = 100
    mystack = SetOfStack(num_of_stacks, stack_size)
    mystack.push(9, 0)
    mystack.push(5, 0)
    mystack.push(3, 0)
    mystack.push(1, 1)
    mystack.push(4, 1)
    mystack.push(7, 1)
    mystack.push(6, 2)
    mystack.push(3, 2)
    mystack.push(5, 2)
    mystack.push(4, 2)

    for stack_num in range(num_of_stacks):
        print(mystack.pop(stack_num))
        print(mystack.pop(stack_num))
        print(mystack.pop(stack_num))
    print(mystack.size())

    mystack = StackWithMin(stack_size)
    mystack.push(6)
    mystack.push(3)
    mystack.push(5)
    mystack.push(4)
    print(mystack.min())

if __name__ == "__main__":
    main()