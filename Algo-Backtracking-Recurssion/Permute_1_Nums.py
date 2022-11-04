"""
PERMUTATION Template

Exactly same as Backtrack.... Find out Breath ---> (low,high) and Depth ----> low+1
Difference is: We need all permutation, so isSafe is always valid!

https://leetcode.com/problems/permutations/solution/
"""
from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first):
            if first >= last:  # A sol is found, make it part of finalres
                finalres.append(nums[:])

            # 2) Breath .... (low, high)
            for i in range(first, last):
                # 3) IsSafe: We want all permutation, so everything's safe      ---> Diff from backtracking for permutations
                # 4) Take this move. Make this guy first
                nums[i], nums[first] = nums[first], nums[i]
                # 5) See if recursively we can reach sol... Depth: First+1
                backtrack(first + 1)
                # 6) Backtrack if this doesn't work
                nums[first], nums[i] = nums[i], nums[first]

        finalres = []
        last = len(nums)
        backtrack(0)
        return finalres

