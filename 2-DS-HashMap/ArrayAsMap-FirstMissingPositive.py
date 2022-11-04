""" https://leetcode.com/problems/first-missing-positive/
DS: Seen Map        Pattern: right num for this index is seen?
DS: Array Indexs!   Pattern: Use ARRAY INDEXES as Map KEYS to store NEW values 
"""
import collections
from typing import List

""" DS: Seen Map     Pattern: right num for this index is seen? """
class Solution:
    def firstMissingPositive_UsingMap(self, nums: List[int]) -> int:
        seen = collections.Counter(nums)
        
        for i in range(len(nums)):
            # For 0th index, 1 should be available
            # for 1st index, 2 should be available
            if (i+1) in seen:   # The right num for this index exits!
                continue
            else:
                return (i+1)
            
        return len(nums)+1  # i+1

    """ Pattern: Use ARRAY INDEXES as Map KEYS to store NEW values 
    """
    def firstMissingPositive(self, nums: List[int]) -> int:
        N = len(nums)
        for i, num in enumerate(nums):
            # Negative or OOB numbers
            if num <= 0 or num > N:    
                nums[i] = 0                 # Useless, mark them 0s   
        print(f"Nums after marking useless: {nums}")
        # Now all nums are in range 0 to N so we can place them at right index

        # Add N to those indexes which are VALID: i.e num is available
        for i, num in enumerate(nums):
            """ PROBLEM: Nums (0) will also be overwritten during iteration so have to differentiate them with condition"""
            # Now each num is in range of 1 to N, add +N into those index
            num = num % (N+1)
            if 1 <= num <= N:
                rightIndex = (num - 1)
                nums[rightIndex] += N + 1       # Add N+1 in rightIndex to mark it VALID
        print(f"Nums after adding +N: {nums}")

        # Now VALID indexes are +N so INVALID indexes can be found as <N values
        for i, num in enumerate(nums):
            if num <= N:
                return i+1
        
        
        # If all indexes are VALID then LAST numer
        return N+1




s = Solution()
nums = [1,2,0]
print(s.firstMissingPositive(nums)) # output: 3 The numbers in the range [1,2] are all in the array.
nums = [3,4,-1,1]
print(s.firstMissingPositive(nums)) # Output: 2 Explanation: 1 is in the array but 2 is missing
nums = [7,8,9,11,12]
print(s.firstMissingPositive(nums)) # Output: 1 Explanation: The smallest positive integer 1 is missing.`

