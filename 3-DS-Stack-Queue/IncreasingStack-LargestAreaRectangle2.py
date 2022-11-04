from STACK import Stack


"""
http://www.geeksforgeeks.org/largest-rectangle-under-histogram/
"""


def LargestRectangleInHistogram(hist):
    s = Stack()
    i = 0
    max_area = 0

    # Scan through Histogram
    while i < len(hist):
        # Increasing ---> Current Hist > Prev Hist
        if s.isEmpty() or hist[i] >= hist[s.peek()]:
            s.push(i)
        # Decreased! ---> Current Hist < Prev Hist (Hisab lagavi do)
        else:
            # Pop hist till Decreasing stops
            while not s.isEmpty() and hist[s.peek()] > hist[i]:
                L = s.pop()
                height = hist[L]
                if s.isEmpty():
                    area = height * i
                else:
                    area = height * (i - s.peek() - 1)
                max_area = max(max_area, area)
            s.push(i)
        i += 1

    while not s.isEmpty():
        L = s.pop()
        height = hist[L]
        area = height * (i - L - 1)
        max_area = max(max_area, area)

    return max_area


"""
Optimized version
"""


def LargestRectangleInHistogram_optimized(hist):
    s = Stack()
    max_area = 0
    i = 0

    # Scan through Histogram
    while i < len(hist):

        # Increasing ---> Current Hist > Prev Hist
        if s.isEmpty() or hist[i] >= hist[s.peek()]:
            s.push(i)
            i += 1
        # Decreased! ---> Current Hist < Prev Hist (Hisab lagavi do)
        else:
            # Pop hist till Decreasing stops
            L = s.pop()

            # Calculate area
            if s.isEmpty():
                current_area = hist[L] * i
            else:
                current_area = hist[L] * (i - s.peek() - 1)

            # Hisab for max area
            max_area = max(max_area, current_area)

    # Consider all remaining histogram
    while not s.isEmpty():
        L = s.pop()

        # Calculate area
        if s.isEmpty():
            current_area = hist[L] * i
        else:
            current_area = hist[L] * (i - s.peek() - 1)

        # Hisab for max area
        max_area = max(max_area, current_area)

    return max_area


hist = [6, 2, 5, 4, 5, 1, 6]
print(LargestRectangleInHistogram(hist))
print(LargestRectangleInHistogram_optimized(hist))

hist = [2, 1, 5, 6, 2, 3]
print(LargestRectangleInHistogram(hist))
print(LargestRectangleInHistogram_optimized(hist))



"""
Nearest Smaller Element

Given an array, find the nearest smaller element G[i] for every element A[i] in the array such that the element has an index smaller than i.

More formally,

G[i] for an element A[i] = an element A[j] such that
    j is maximum possible AND
    j < i AND
    A[j] < A[i]
Elements for which no smaller element exist, consider next smaller element as -1.

Example:

arr = [4, 5, 2, 10]
result = [-1, 4, -1, 2]


arr = [3, 2, 1]
result = [-1, -1, -1]
"""


def Nearest_Smallest(arr):
    result = [-1] * len(arr)
    s = Stack()
    s.push(-1)

    # Scan through entire Array
    for index in range(len(arr)):

        # Nearest value is lesser ? Choose it
        if arr[index] > s.peek():
            result[index] = s.peek()
        else:
            # Go till the prev nearest value that's lesser? Choose it
            while arr[index] > s.peek():
                s.pop()
            result[index] = s.peek()

        # Get ready for next iteration
        s.push(arr[index])

    return result

arr = [4, 5, 2, 10]
print(Nearest_Smallest(arr))

arr = [4, 5, 6, 1, 2]
print(Nearest_Smallest(arr))

arr = [4, 2, 10, 6, 5]
print(Nearest_Smallest(arr))

arr = [3, 2, 1]
print(Nearest_Smallest(arr))

arr = [1, 3, 0, 2, 5]
print(Nearest_Smallest(arr))
