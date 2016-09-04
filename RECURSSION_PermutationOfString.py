def AddCharAtIndex(word, c, index):
    start = word[0:index]
    end = word[index]
    return start + c + end


def getAllPermute(str):
    result = []
    if str is None:
        return None
    elif len(str) == 0:
        result.append("")
        return result
    elif len(str) == 1:
        result.append(str[0])
        return result
    first = str[0]
    remaining = str[1:len(str)]
    print first, remaining
    listOfPerm = getAllPermute(remaining)
    for word in listOfPerm:
        for i in xrange(len(word)):
            result.append(AddCharAtIndex(word, first, i))
    return result


def main():
    str = 'abc'
    print getAllPermute(str)

if __name__ == "__main__":
    main()
