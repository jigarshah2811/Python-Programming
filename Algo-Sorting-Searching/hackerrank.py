"""
https://leetcode.com/problems/k-diff-pairs-in-an-nums/
"""

import collections
class Solution:
    def findPairs(self, nums, diff):
        """
        Returns the number of pairs in nums that differ by diff.
        See problem statement for description of algorithm.
        nums: list of unique integers
        diff: integer, the targeted difference
        return: number of pairs realizing the difference
        """
        n = len(nums)

        # Edge cases
        if n < 2:
            return 0

        pairs = set()

        d = collections.Counter(nums)

        for num in nums:
            rem = num+diff
            if (diff > 0 and rem in d) or (diff == 0 and d[rem]>1):     #### TRICK: When diff = 0, the rem freq should be > 1 (dups)
                pairs.add((num, rem))
                d[rem] -= 1

        return len(pairs)


s = Solution()
nums = [3, 1, 4, 1, 5]
print(s.findPairs(nums, 2))
nums = [1, 2, 3, 4, 5]
print(s.findPairs(nums, 1))
nums = [1, 3, 1, 5, 4]
print(s.findPairs(nums, 0))