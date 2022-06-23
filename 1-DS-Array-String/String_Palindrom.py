from STACK import Stack

def main():
    str = "AppleKayaKnothingAvid divA"
    mystack = Stack()
    mystack.push(str[0])
    ele = []

    for i in range(1, len(str)-1):
        if str[i+1] == mystack.peek():
            ele.append(mystack.pop())
        else:
            mystack.push(str[i])

    total = mystack.size()
    end = len(str) - 1

    print("Palindrom strings:")
    for i in range(total):
        palindrom = ""
        temp = mystack.pop()
        while str[end] != temp:
            palindrom += str[end]
            end -= 1
        print(palindrom)
        end -= 1

if __name__ == "__main__":
    main()
