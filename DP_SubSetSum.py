"""
http://www.geeksforgeeks.org/find-subarray-with-given-sum/

Find subarray with given sum | Set 1 (Nonnegative Numbers)
Given an unsorted array of nonnegative integers, find a continous subarray which adds to a given number.

Examples:

Input: arr[] = {1, 4, 20, 3, 10, 5}, sum = 33
Ouptut: Sum found between indexes 2 and 4

Input: arr[] = {1, 4, 0, 0, 3, 10, 5}, sum = 7
Ouptut: Sum found between indexes 1 and 4

Input: arr[] = {1, 4}, sum = 0
Output: No subarray found
"""


def findSumPositives(arr, sum):
    currentSum = arr[0]

    for i in xrange(1, len(arr)):

        # Remove ele if sum becomes higher
        start = i
        while currentSum > sum and start < i:
            currentSum -= arr[start]

        if currentSum == sum:
            print "Founds sum from indexes {0} to {1}".format(start, i)
        currentSum += arr[i]





"""
http://www.geeksforgeeks.org/find-if-there-is-a-subarray-with-0-sum/
Given an array of positive and negative numbers, find if there is a subarray (of size at-least one) with 0 sum.

Input: {4, 2, -3, 1, 6}
Output: true
There is a subarray with zero sum from index 1 to 3.

Input: {4, 2, 0, 1, 6}
Output: true
There is a subarray with zero sum from index 2 to 2.

Input: {-3, 2, 3, 1, 6}
Output: false
There is no subarray with zero sum.
"""

"""
arr[] = {1, 4, -2, -2, 5, -4, 3}

If we consider all prefix sums, we can
notice that there is a subarray with 0
sum when :
1) Either a prefix sum repeats or
2) Or prefix sum becomes 0.

Prefix sums for above array are:
1, 5, 3, 1, 6, 2, 5
"""

"""
Method 1: PowerSet - Consider all possible subsets of a powerset
"""


def powerSet(arr):
    thisSet = []

    # Total number of sets
    for counter in xrange(pow(2, len(arr))):
        # Ele to consider in set or not
        for index in xrange(len(arr)):
            if counter & (1 << index):
                thisSet.append(arr[index])
        print thisSet
        thisSet = []


def powerSetSum(arr):
    thisSet = []

    # Total number of sets
    for counter in xrange(pow(2, len(arr))):
        # Ele to consider in set or not
        for index in xrange(len(arr)):
            if counter & (1 << index):
                thisSet.append(arr[index])
        if sum(thisSet) == 0:
            print thisSet
        thisSet = []

"""
Using Hash
"""


def subArraySumZero(arr):
    d = dict()  # To storage 'visited sum'
    sum = 0

    for i in xrange(len(arr)):
        sum += arr[i]

        # If Sum exists, removing that many ele will result in 0
        if sum == 0 or sum in d:
            print "True: Found Subarray sums to zero from SubArray {0}".format(arr[d[sum]+1:i+1])
        else:
            # Store this sum as visited
            d[sum] = i

"""
Using DP
"""


def subArraySumZeroRecur_Util(sumA, A, index):
    # BASE CASE
    if index >= len(A):
        return False
    # Check if the SubSet in consideration makes sum=0
    if sumA != [] and sum(sumA) == 0:
        print sumA

    tmpA = list(sumA)
    sumA.append(A[index])
    return subArraySumZeroRecur_Util(sumA, A, index + 1) \
        or subArraySumZeroRecur_Util(tmpA, A, index + 1)


def subArraySumZeroRecur(A):
    sumA = []
    index = 0
    subArraySumZeroRecur_Util(sumA, A, index)


# arr = ['a', 'b', 'c']
# powerSet(arr)

sum = 23
arr = [5, 2, 4, 8, 9, 5, 10, 23]
findSumPositives(arr, sum)

"""
print "PowerSetSum = "
arr = [1, 4, -2, -2, 5, -4, 3]
powerSetSum(arr)


# subArraySumZero(arr)
print "subArraySumZeroRecur = "
subArraySumZeroRecur(arr, sum)
"""

