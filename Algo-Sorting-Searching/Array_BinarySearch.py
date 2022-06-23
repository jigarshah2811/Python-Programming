import collections
import sys

"""
Regular Binday Search
"""

class Solution(object):
    def binsearch(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) >> 1
            if target == nums[mid]:
                return mid

            elif target > nums[mid]:
                # Target must be on Right side
                low = mid + 1
            else:
                # Target must be on left side
                high = mid - 1
        return -1

    def binsearch_nolen(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        low = 0
        high = sys.maxsize

        while low <= high:
            mid = (low + (high - low)) >> 1
            if target == nums[mid]:
                return mid

            elif target > nums[mid]:
                # Target must be on Right side
                low = mid + 1
            else:
                # Target must be on left side
                high = mid
        return -1


def BinarySearch(array, valueToFind):
    low = 0
    high = len(array) - 1
    while low < high:
        mid = (low + high) / 2 # mid = (low+hign)<<1
        if array[mid] == valueToFind:
            print("Found value {0} at index: {1}".format(valueToFind, mid))
            return mid
        elif array[mid] < valueToFind:
            print("search in RIGHT half")
            low = mid + 1
        else:
            print("search in LEFT half")
            high = mid - 1
    print("Value {0} not found".format(valueToFind))
    return -1   # not found


"""Tweaked Binday Search:

If multiple values are same as valueToFind, 
return the lowest index instead of 1st hit in binary search

"""
def BinarySearch_LowestIndex(array, valueToFind):
    low = 0
    high = len(array) - 1
    result = -1 # not found by default

    while low < high:
        mid = (low + high) / 2
        if array[mid] == valueToFind:
            print("Found value {0} at index: {1}... Still searching lower index".format(valueToFind, mid))
            result = mid
            high = mid - 1              ###### TIP: tweak BS: CONTINUE SEARCHING ON LEFT HALF
        elif array[mid] < valueToFind:
            print("search in right half")
            low = mid + 1
        else:
            print("search in left half")
            high = mid - 1
    return result


def BinarySearch_HighestIndex(array, valueToFind):
    low = 0
    high = len(array) - 1
    result = -1  # not found by default

    while low < high:
        mid = (low + high) / 2  # mid = (low+hign)<<1
        if array[mid] == valueToFind:
            print("Found value {0} at index: {1}... Still searching higher index".format(valueToFind, mid))
            result = mid
            low = mid + 1  ###### TIP: tweak BS: CONTINUE SEARCHING ON RIGHT HALF
        elif array[mid] < valueToFind:
            print("search in right half")
            low = mid + 1
        else:
            print("search in left half")
            high = mid - 1
    return result  # not found


"""
https://leetcode.com/problems/search-in-rotated-sorted-array
Search in Rotated Sorted Array

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
"""
def BinarySearch_SortedRotatedArray(array, valueToFind):
    low = 0
    high = len(array)-1

    while low <= high:
        mid = (low + high) >> 1
        if array[mid] == valueToFind:
            return mid

        if array[low] <= array[mid]:
            # LEFT half is Sorted. Perform regular ops
            if array[low] <= valueToFind <= array[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            # RIGHT half is sorted. Perform regular ops but inverted
            if array[mid] <= valueToFind <= array[high]:
                low = mid + 1
            else:
                high = mid - 1
    return -1






def main():
    """
    a = [1, 3, 5, 6, 8, 10, 10, 10, 12]
    valueToFind = 10
    result = BinarySearch(a, valueToFind)
    if result == -1:
        print "Value {0} Not found".format(valueToFind)
    else:
        print "Found {0} at location Index {1}".format(valueToFind, result)

    result = BinarySearch_LowestIndex(a, valueToFind)
    if result == -1:
        print "Value {0} Not found".format(valueToFind)
    else:
        print "Found {0} at location Index {1}".format(valueToFind, result)

    result = BinarySearch_HighestIndex(a, valueToFind)
    if result == -1:
        print "Value {0} Not found".format(valueToFind)
    else:
        print "Found {0} at location Index {1}".format(valueToFind, result)

    sumToFind = 14
    low, high = FindPairWithSum(a, sumToFind, 0, len(a)-1)
    if low == -1 or high == -1:
        print "Sum {0} Not found".format(sumToFind)
    else:
        print "Sum {0} found at pair of index {1} and {2}".format(sumToFind, low, high)

    sumToFind = 16
    for i in xrange(0, len(a)-1):
        low, high = FindPairWithSum(a, sumToFind-i, i, len(a)-1)
        if low != -1 and high != -1:
            print "Sum {0} found at index {1} {2}".format(sumToFind, low, high)


    index = BinarySearch_SortedRotatedArray([4, 5, 6, 7, 0, 1, 2, 3], 0)
    print "Index found: {0}".format(index)
    index = BinarySearch_SortedRotatedArray([4, 5, 6, 7, 0, 1, 2, 3], 7)
    print "Index found: {0}".format(index)
    index = BinarySearch_SortedRotatedArray([5 ,1, 3], 5)
    print "Index found: {0}".format(index)
    index = BinarySearch_SortedRotatedArray([5, 1, 3], 1)
    print "Index found: {0}".format(index)
    index = BinarySearch_SortedRotatedArray([5, 1, 3], 3)
    print "Index found: {0}".format(index)
    index = BinarySearch_SortedRotatedArray([5, 1, 3], 0)
    print "Index found: {0}".format(index)
    """


if __name__ == "__main__":
    s = Solution()
    nums = [-1,0,3,5,9,12]
    print(("Find 9, index: {0}".format(s.binsearch(nums, 9))))
    nums = [5]
    print(("Find 5, index: {0}".format(s.binsearch(nums, 5))))
