"""
https://leetcode.com/articles/group-anagrams/
"""
import collections
class Solution:
    def groupAnagrams(self, strs):
        """
        Tuple Map!
        # Example: {('a','e','t'): ["eat", "tea", "ate"]}
        """
        tupleMap = collections.defaultdict(list)

        # Build map from strings, using each string's unique tuple
        for s in strs:
            key = tuple(sorted(s))
            tupleMap[key].append(s)

        # All anagram strings (values) are now against the SAME tuple key
        return list(tupleMap.values())

    def groupAnagramsFreq(self, strs):
        # Map: { (26 chars freq in str) : [strings] }
        # Example: {(2, 1, 0, 0, ...., 0) : ["aab", "aba", "baa"] }
        freqTupleMap = collections.defaultdict(list)

        # Build map from strings, using each string's unique tuple
        for s in strs:
            freqChars = [0]*26
            for c in s:
                freqChars[ord(c)-ord('a')] += 1

            key = tuple(freqChars)
            freqTupleMap[key].append(s)

        # All anagram strings (values) are now against the SAME freq tuple of chars
        return list(freqTupleMap.values())

    def isAnagram(self, s, t):
        return sorted(s) == sorted(t)

    def isAnagramTuple(self, s, t):
        tuple(sorted(s)) == tuple(sorted(t))


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
s = Solution()
print((s.groupAnagrams(strs)))
print((s.groupAnagramsFreq(strs)))
