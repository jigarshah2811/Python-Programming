"""
567. Permutation in String

https://leetcode.com/problems/permutation-in-string/solution/


Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.
Example 1:
Input:s1 = "ab" s2 = "eidbaooo"
Output:True
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:
Input:s1= "ab" s2 = "eidboaoo"
Output: False
Note:
The input strings only contain lower case letters.
The length of both given strings is in range [1, 10,000].
"""

class Solution(object):
    def findPerm(self, text, pattern):
        "Since we have limited number of Chars available, we can use Array for size 'a' to 'z'"
        freqPattern = [0]*1000
        freqText = [0]*1000
        result = []

        # 1st pattern match
        for i in range(len(pattern)):
            freqPattern[ord(pattern[i])] += 1
            freqText[ord(text[i])] += 1

        # All subsequent pattern match
        for i in range(0, len(text)-len(pattern)+1):
            if freqPattern == freqText:
                result.append(i)
            # Add new char freq for next window
            # Remove old char freq from previous window
            freqText[ord(text[i])] += 1
            freqText[ord(text[i-len(pattern)])] -= 1

        return result




print(Solution().findPerm("cbaebabacd", "abc"))
print(Solution().findPerm("abab", "ab"))
print(Solution().findPerm("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "a"))
