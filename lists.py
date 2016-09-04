List1 = [4, 10, 15, 24, 26] 
List2 = [0, 9, 12, 20] 
List3 = [5, 18, 22, 30]


def main():
    ranges = list()
    rangeMin = rangeMax = 0

    minListLen = min(len(List1), len(List2), len(List3))
    
    l1 = l2 = l3 = 0

    while l1 < xrange(5) and l2 < xrange(4) and l3 < xrange(4):
    # for (l1, l2, l3) in (xrange(len(List1)), xrange(len(List2)), xrange(len(List3))):
        while List1[l1] <= rangeMax:
            l1 += 1
        while List2[l2] <= rangeMax:
            l2 += 1
        while List3[l3] <= rangeMax:
            l3 += 1

        rangeMin = min(List1[l1], List2[l2], List3[l3])
        rangeMax = max(List1[l1], List2[l2], List3[l3])
        ranges.append((rangeMin, rangeMax))

    print ranges

if __name__ == "__main__":
    main()
