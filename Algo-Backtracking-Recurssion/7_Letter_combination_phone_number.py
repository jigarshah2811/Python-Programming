"""
######### ------- BACKTRACKING -----------#########

Visual explanation: https://leetcode.com/problems/letter-combinations-of-a-phone-number/solution/

"""
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        phoneMap = {'2': ['a', 'b', 'c'],
                    '3': ['d', 'e', 'f'],
                    '4': ['g', 'h', 'i'],
                    '5': ['j', 'k', 'l'],
                    '6': ['m', 'n', 'o'],
                    '7': ['p', 'q', 'r', 's'],
                    '8': ['t', 'u', 'v'],
                    '9': ['w', 'x', 'y', 'z']}

        def backtrack(begin, res):
            # 1) Base case: If we found one comb, get in finalRes and return
            if len(res) == len(digits):
                finalres.append("".join(res))
                res = []
                return

            # 2) BREATH --> Try all letters mapped to this digit
            for letter in phoneMap[digits[begin]]:
                # 3) If safe: We need all combination so each permutation is safe to consider

                # 4) Take the move: get this letter in res
                res.append(letter)
                # 5) With this letter from digit[0], recur for all letters of digit[1]
                # Depth -->
                backtrack(begin + 1, res)
                # 6) Backtrack: Remove this letter and try others
                res.pop()

            return finalres

        finalres = []
        if digits:
            backtrack(0, [])
        return finalres

s = Solution()
print(('krups' in s.letterCombinations("57877")))   # krups
print(('jigar' in s.letterCombinations("54427")))    # jigar

"""
# APPROACH: Iterative
#l1 = list("abc")
#l2 = list("def")
"""
"""
l1 = ['a', 'b', 'c']
l2 = ['d', 'e', 'f']
l3 = ['g', 'h', 'i']

comb_list = [s1 + s2 for s1 in l1 for s2 in l2]
result = [comb+s3 for comb in comb_list for s3 in l3]
# print comb_list
# print result
"""