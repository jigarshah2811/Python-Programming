"""
POWERSET = backtracking in iterative !!

Basically, consider all 2^n permutations of a series
Include/Exclude based on weather corresponding bitPos is 1 or 0

series  ---> [1, 2, 3]
bitPos  ---> [0, 0, 0]
        ---> [0, 0, 1]      # Include [3]
        ---> [0, 1, 0]      # Include [2]
        ---> [0, 1, 1]      # Include [2, 3]
        ---> [1, 0, 0]
        ---> [1, 0, 1]
        ---> [1, 1, 0]
        ---> [1, 1, 1]

https://leetcode.com/problems/subsets/submissions/
"""
from typing import List

class Solution(object):
    def powerSet(self, nums):
        res = []
        subSet = []
        n = len(nums)

        for counter in range(pow(2, n)):
            for bitIndex, num in enumerate(nums):
                #print "i:{0}, j:{1}".format(i, j)
                if counter & (1 << bitIndex):
                    subSet.append(num)
            res.append(subSet)
            subSet = []

        return res


s = Solution()
nums = [1,2,3]
print(("PowerSet: ", s.powerSet(nums)))

class SolutionIterative:
    def letterCasePermutation(self, S: str) -> List[str]:
        powerSet = [S]

        for i, c in enumerate(S):
            if c.isalpha():
                sol1 = [subset[:i] + subset[i].swapcase() + subset[i + 1:] for subset in powerSet]
                powerSet.extend(sol1)

        return powerSet


class SolutionRecur:
    def letterCasePermutation(self, S: str) -> List[str]:
        subset, powerSet = [], []

        def backtrack(S, i):
            # 1) Base case: If i reaches end
            if i >= len(S):
                print(("Found result: ", S))
                powerSet.append(S)
                return

            # 2) Breath ---> Lower() and Upper()
            # 3) IfSafe
            if S[i].isalpha():
                backtrack(S[:i] + S[i].lower() + S[i+1:], i + 1)
                backtrack(S[:i] + S[i].upper() + S[i+1:], i + 1)
            else:
                backtrack(S, i+1)

        backtrack(S, i=0)
        return powerSet


s = SolutionIterative()
print(("Letter Combination: ", s.letterCasePermutation("a1b2")))

s = SolutionRecur()
print(("Letter Combination: ", s.letterCasePermutation("a1b2")))

