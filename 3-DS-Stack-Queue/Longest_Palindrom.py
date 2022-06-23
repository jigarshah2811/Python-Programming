from STACK import Stack
def longestPalindrom(query):
    maxPaliLen = 0
    paliLenSoFar = 0
    middleOfPalin = False
    start, end = 0, 0
    popping = False
    maxPaliStr = ""

    s = Stack()

    while end < len(query)-1:

        if s.isEmpty() or (query[end] != s.peek() and query[end+1] != s.peek()):
            # Not a palindrom candidate
            s.push(query[end])
            start = end

        else:
            print("popping at: {0}".format(query[end]))
            s.pop()
            start -= 1
            maxPaliLen = max(maxPaliLen, end - start + 1)
            maxPaliStr = query[start:end]

        end += 1

    print(maxPaliStr)
    return maxPaliLen

s = 'kayak'
print(longestPalindrom(s))
s = 'alacala'
print(longestPalindrom(s))
s = 'somekayaktempalacalaxyz'
print(longestPalindrom(s))
