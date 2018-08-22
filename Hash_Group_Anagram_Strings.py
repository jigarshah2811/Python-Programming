import collections

"""
https://leetcode.com/articles/group-anagrams/

Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.

"""
class Solution(object):
    def groupAnagram(self, queries):

        d = {}
        # Iterate thorugh each string
        for i in xrange(len(queries)):
            # Sort (To find anagram) and see if anagram already exists in dict
            sortedQuery = sorted(queries[i])
            sortedStr = "".join(sortedQuery)
            try:
                # Store index of original string
                d[sortedStr].append(i)
            except:
                d[sortedStr] = [i]




        # Now dict has all anagram -> [indexes]
        # Print the strings according to indexes so anagrams will be grouped together
        result = []
        for sortedStr, listIndexes in d.items():
            group = []
            for i in listIndexes:
                group.append(queries[i])
            result.append(group)

        return result

    def groupAnagram_Optimized(self, queries):
        # Dict initialization {key: []}
        d = collections.defaultdict(list)
        for query in queries:
            # sorted(query) will return list
            # But list is NOT hashable in dict, So we convert it into Tuple!
            # Store into dict
            # Example: {('a','e','t'): ["eat", "tea", "ate"]}
            d[tuple(sorted(query))].append(query)
        return d.values()

    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return sorted(s) == sorted(t)

input = ["eat", "tea", "tan", "ate", "nat", "bat"]
print Solution().groupAnagram(input)
print Solution().groupAnagram_Optimized(input)
