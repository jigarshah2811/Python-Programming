def AllPossibleComb(str):
    s = list(str)
    pos = list()

    for i in range(len(s)):
        # Count ?
        if s[i] == '?':
            pos.append(i)

    print("Indexes having ? --> {}".format(pos))

    SuperSet = list()

    # Power set of possible Que
    for i in range(pow(2, len(pos))):
        subset = s

        for posIndex in range(len(pos)):
            # Replace ? with that positions bit from PowerSet
            if i & (1 << posIndex):
                # Bit is 1
                subset[pos[posIndex]] = 1
            else:
                # Bit is 0
                subset[pos[posIndex]] = 0
        print(subset)

    return SuperSet

str = "0?1??"
print(AllPossibleComb(str))

"""
set_size = 2
for i in xrange(pow(2, set_size)):
    for j in xrange(set_size):
        if (1 << j) & i:
            print 1
        else:
            print 0
"""