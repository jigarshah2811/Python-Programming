"""
STRATEGY: Sliding window (Find localMin, localMax and txn.... Keep going)
"""

def FindMaxValid(str):
    maxValid = 0
    maxValidSoFar = 0
    count = 0

    start = end = 0
    print(str)
    for end in range(len(str)):
        if str[end] == "(":
            count += 1

        else:
            if count > 0:
                count -= 1
                maxValidSoFar += 2
                start = end + 1

        print("Got: {0} Count: {1}".format(str[end], count))
        if count == 0:
            # Hisab
            # Reset indexes
            start = end+1

    maxValid = max(maxValid, maxValidSoFar)
    return maxValid

str = "(())"
assert(FindMaxValid(str) == 4)

str = "(())"
assert(FindMaxValid(str) == 4)

str = "(())()"
assert(FindMaxValid(str) == 6)

# INVALID
str = "(())("
assert(FindMaxValid(str) == 4)

str = "))))()())("
assert(FindMaxValid(str) == 4)

str = "))))()())("
assert(FindMaxValid(str) == 4)

str = ")()()(((()))("
print(FindMaxValid(str))