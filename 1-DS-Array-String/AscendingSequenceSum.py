from typing import List


""" Pattern: Keep track of curSum and maxSum 
https://leetcode.com/problems/maximum-ascending-subarray-sum/submissions/
"""
class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        
        curSum, maxSum = 0, 0
        for i, num in enumerate(nums):
            if num > nums[i-1]:      # Ascending order continues
                curSum += num
            else:                    # Ascending stoped, restart
                curSum = num
            
            # Keep track of maxSum seen by far
            maxSum = max(maxSum, curSum)
        
        return maxSum

"""
Next: https://leetcode.com/problems/find-good-days-to-rob-the-bank/`
"""