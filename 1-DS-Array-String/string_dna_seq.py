"""
REPEATED DNA SEQUENCE

https://leetcode.com/problems/repeated-dna-sequences/
"""

import collections
class Solution:
    def findRepeatedSequence(self, s):
        #edge cases
        if len(s) < 10:
            return []

        seen = dict()
        res = set()

        for i in range(len(s)):
            subStr = s[i:i+10]
            if subStr in seen:
                res.add(subStr)
            else:
                seen[subStr] = True
        return list(res)

str = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
s = Solution()
print((s.findRepeatedSequence(str)))