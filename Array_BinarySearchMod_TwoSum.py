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
    def twoSumUnsorted(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = list()
        d = dict((nums[i], i) for i in xrange(len(nums)))
        #print d

        low = 0
        high = len(nums) - 1

        for index in xrange(len(nums)):
            reminder = target - nums[index]
            if reminder in d and d[reminder] != index:
                result.append(index)
                result.append(d[reminder])
                return result

        return result

    def twoSumSorted(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # print numbers
        low = 0
        high = len(numbers) - 1

        res = []
        while low < high:
            if numbers[low] + numbers[high] == target:
                res.append(low + 1)
                res.append(high + 1)
                return res
            elif numbers[low] + numbers[high] > target:
                high -= 1
            else:
                low += 1
        return res

nums = [3,2,4]
target = 6
print Solution().twoSumUnsorted(nums, target)
print Solution().twoSumSorted(sorted(nums), target)

nums = [3, 3]
target = 6
print Solution().twoSumUnsorted(nums, target)
print Solution().twoSumSorted(sorted(nums), target)

