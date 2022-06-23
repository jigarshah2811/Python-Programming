import heapq
List1 = [4, 10, 15, 24, 26]
List2 = [0, 9, 12, 20] 
List3 = [5, 18, 22, 30]


def main():
    ranges = list()

    for l1, l2, l3 in zip(List1, List2, List3):
        heap = []
        heapq.heappush(heap, l1)
        heapq.heappush(heap, l2)
        heapq.heappush(heap, l3)
        print(heapq.heappop(heap))
        #print heapq.heapify(heap)

        rangeMin = min(l1, l2, l3)
        rangeMax = max(l1, l2, l3)
        ranges.append((rangeMin, rangeMax))


    print(ranges)

if __name__ == "__main__":
    main()
