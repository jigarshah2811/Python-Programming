"""
STRATEGY: Sort, Map
"""

class Solution(object):
    # Remove dup from SORTED Arr?
    def removeDuplicates(self, nums):
        i = 1
        lenNums = len(nums)

        while i < lenNums:
            if nums[i] == nums[i - 1]:
                del nums[i - 1]
                lenNums -= 1
            else:
                i += 1

        return nums

    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        d = dict()
        for num in nums:
            if num in d:
                return True
            d[num] = True

        return False

s = Solution()
print((s.containsDuplicate([3,5,1,3,5,7,8])))
print((s.removeDuplicates([0,0,1,1,1,2,2,3,3,4])))
print((s.removeDuplicates([1,1,2])))

# Remove dup from UNSORTED Arr?
# Sorting array and check pairs; O(NlogN) time, O(1) space
# Using hash-set or hash-map; O(N) time, O(N) space
# If there are only one duplicate and numbers [0 <= x < n], you will use XOR operation to find duplicate; otherwise if numbers around [1 <= x < n] use Cycle detection approach; O(N) time O(1) space