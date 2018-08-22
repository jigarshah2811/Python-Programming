"""
Group Shifted String

https://www.geeksforgeeks.org/group-shifted-string/
https://www.programcreek.com/2014/05/leetcode-group-shifted-strings-java/

Given an array of strings (all lowercase letters), the task is to group them in such a way that all strings in a group are shifted versions of each other. Two string S and T are called shifted if,

S.length = T.length
and
S[i] = T[i] + K for
1 <= i <= S.length  for a constant integer K
For example strings {acd, dfg, wyz, yab, mop} are shifted versions of each other.

Input  : str[] = {"acd", "dfg", "wyz", "yab", "mop",
                 "bdfh", "a", "x", "moqs"};

Output : a x
         acd dfg wyz yab mop
         bdfh moqs
All shifted strings are grouped together.
"""
import collections
class Solution(object):
    def groupShiftedStrs(self, strs):
        d = collections.defaultdict(list)

        for str in strs:
            diff = self.getDiff(str)

            # Make diff as tuple(Key) and value as list of strings with THAT diff
            d[diff].append(str)

        # print d
        return d.values()

    def getDiff(self, str):
        listDiff = []

        """
        Calc distrance (diff) between chars within string
        [a,c,d] = [2, 1]
        [d,f,g] = [2, 1]
        [m,o,p] = [2, 1]
        """
        for i in xrange(1, len(str)):
            oneDiff = ord(str[i]) - ord(str[i-1])
            listDiff.append(oneDiff)
        return tuple(listDiff)


strs = ["acd", "dfg", "wyz", "yab", "mop", "bdfh", "a", "x", "moqs"]
print Solution().groupShiftedStrs(strs)
