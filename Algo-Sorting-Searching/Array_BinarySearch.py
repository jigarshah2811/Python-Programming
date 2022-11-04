import collections
import sys

"""
Regular Binday Search
"""

class Solution(object):
    def binsearch(self, nums, target):
        low, high = 0, len(nums)-1

        while low < high:
            mid = (low + high) >> 1
            if target == nums[mid]:     # Check if target is HERE
                return mid              # FOUND Target, Bingo

            elif target > nums[mid]:    # Target is HIGHER?                                        
                low = mid + 1       # Search on R ----->
            else:                       # Target is LOWER?                                        
                high = mid - 1      # Search on <------- L
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

"""Tweaked Binday Search:

If multiple values are same as target, 
return the lowest index instead of 1st hit in binary search

"""
def BinarySearch_LowestIndex(nums, target):
    low, high = 0, len(nums)-1

    result = -1     # Not found by default
    while low < high:
        mid = (low + high) >> 1
        if target == nums[mid]:
            # Trick: This can be one of the dup, we still want to find the first occurance 
            result = mid
            high = mid - 1 # Keep searching on <------ L side
        elif target > nums[mid]:    # Target is Higher, must be on R ---> side
            low = mid + 1
        else:                       # Target is Lower, must be on <------ L side
            high = mid - 1

    return result
    """ Follow Up: Can you write BS for Last Occurance? """


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
def BinarySearch_SortedRotatedArray(nums, target):
    low = 0
    high = len(nums)-1

    while low <= high:
        mid = (low + high) >> 1
        if nums[mid] == target:
            return mid

        if nums[low] <= nums[mid]:
            # LEFT half is Sorted. Perform regular ops
            if nums[low] <= target <= nums[mid]:
                high = mid - 1          # <----- L Search Left Half
            else:
                low = mid + 1           # ---->  R Search Right Half
        else:
            # RIGHT half is sorted. Perform regular ops but inverted
            if nums[mid] <= target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1
    return -1






def main():
    """
    a = [1, 3, 5, 6, 8, 10, 10, 10, 12]
    target = 10
    result = BinarySearch(a, target)
    if result == -1:
        print "Value {0} Not found".format(target)
    else:
        print "Found {0} at location Index {1}".format(target, result)

    result = BinarySearch_LowestIndex(a, target)
    if result == -1:
        print "Value {0} Not found".format(target)
    else:
        print "Found {0} at location Index {1}".format(target, result)

    result = BinarySearch_HighestIndex(a, target)
    if result == -1:
        print "Value {0} Not found".format(target)
    else:
        print "Found {0} at location Index {1}".format(target, result)

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
