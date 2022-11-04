import collections
"""
https://leetcode.com/problems/two-sum/description/

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

"""

class Solution(object):
    """
    Find Two elements in array that sums to given target sum
    Solution: using Map seen{value-->index}
    """
    def twoSumUnsorted_Map(self, nums, target):
        seen = {}

        # Map: {Value --> Index}
        for i, val in enumerate(nums):
            reminder = target - val
            # Reminder is already in array?
            if reminder in seen:
                return [seen[reminder], i]
            else:
                seen[val] = i

        # not found
        return [-1, -1]

    """
    Find Two elements in SORTED array that sums to given target sum
    Solution: using Binary search, 2 pointers
    """
    def twoSumSorted_BinarySearch(self, nums, target):
        low, high = 0, len(nums)-1
        nums.sort()
        while low < high:
            currentSum = nums[low] + nums[high]
            if target == currentSum:
                return [low, high]
            elif target > currentSum:
                low += 1
            else:
                high -= 1

        # not found
        return [-1, -1]

    """
    Find Three elements in array that sums to given target sum
    Solution: using Map seen{value-->index}
    """
    def threeSum_HashMap(self, nums, target):
        result = set()
        d = collections.defaultdict(list)

        # Sort numbers to do BinarySearch
        nums.sort()
        # Build dict with indexes of numbers, to find 3rd (remaining sum) number fast
        for i in range(len(nums)):
            d[nums[i]].append(i)

        low = 0
        high = len(nums) - 1

        while low < high:
            currentSum = nums[low] + nums[high]     # 1st 2 nums, low & high index
            remEle = target - currentSum            # 3rd remaining num
            if remEle in d:                         # Found!
                for index in d[remEle]:             # There can be dups of same number
                    if index != low and index != high:
                        result.add(sorted([nums[low], nums[high], remEle]))
                low += 1
                high -= 1
            elif currentSum < target:               # too low, Move --->
                low += 1
            else:                                   # too high, move <---
                high -= 1


        return result

    """
    Find Three elements in array that sums to given target sum
    Solution: using Binary Search: Three pointers
    """
    def threeSum_threePointers(self, nums, target):
        result = set()
        n = len(nums)
        nums.sort()

        for i in range(n-2):    # Fix 1 num
            low = i+1       # We always start the left pointer from i+1 because the 0~i has already been tried. [2]
            high = n-1

            while low < high:   # Find other 2 nums for this fixed num
                currentSum = nums[i] + nums[low] + nums[high]
                if currentSum == target:        # Bingo! We found 3 pointers, fixed: i, low and high that totals target!
                    result.add([nums[i], nums[low], nums[high]])
                    low += 1
                    high -= 1
                elif currentSum < target:   # too low, Move --->
                    low += 1
                else:
                    high -= 1               # too high, move <---

        return list(result)


nums = [3,2,4]
print(Solution().twoSumUnsorted_Map(nums, 6))
print(Solution().twoSumSorted_BinarySearch(sorted(nums), 6))

nums = [3, 3]
print(Solution().twoSumUnsorted_Map(nums, 6))
print(Solution().twoSumSorted_BinarySearch(sorted(nums), 6))

nums = [2, 7, 11, 15]
print(Solution().twoSumUnsorted_Map(nums, 9))
print(Solution().twoSumSorted_BinarySearch(sorted(nums), 9))

nums = [-1, 0, 1, 2, -1, -4]
print(Solution().threeSum_threePointers(nums, 0))