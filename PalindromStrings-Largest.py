from STACK import Stack


def main():
    str = "what is avid diva when kayak agree"
    mystack = Stack()
    mystack.push(str[0])
    mymap = {}
    PalindromStartIndexList = []

    sizeOfPalindromStr = 0
    for i in xrange(1, len(str)-1):
        if str[i+1] == mystack.peek():
            # MATCH, Palindrom starts
            if sizeOfPalindromStr == 0:
                PalindromStartIndexList.append(i)
            mystack.pop()
            sizeOfPalindromStr += 1
        else:
            if len(PalindromStartIndexList) != 0:
                mymap[PalindromStartIndexList.pop()] = (sizeOfPalindromStr-1)
            sizeOfPalindromStr = 0
            mystack.push(str[i])

    # get max from mymap accordig to size
    IndexForLargestPalindrom = max(mymap, key=mymap.get)
    SizeOfLargestPalindrom = mymap[IndexForLargestPalindrom]

    # Build largest palindrom string using index and size
    LargestPalindromStr = ""
    PartPalindromStr = ""

    for i in xrange(IndexForLargestPalindrom+1, IndexForLargestPalindrom+1+SizeOfLargestPalindrom):
        PartPalindromStr += str[i]

    LargestPalindromStr = PartPalindromStr[::-1] + str[IndexForLargestPalindrom] + PartPalindromStr
    print LargestPalindromStr


if __name__ == "__main__":
    main()
