import sys


def isPalindrom(myStr):
    reversedList = list(myStr)
    reversedList.reverse()
    originalList = list(myStr)
    return cmp(reversedList, originalList)


def main(args):
    print True if isPalindrom(args[1]) == 0 else False

if __name__ == "__main__":
    main(sys.argv)
