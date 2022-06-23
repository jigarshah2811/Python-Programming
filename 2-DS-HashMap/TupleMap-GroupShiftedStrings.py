"""
Group Shifted String

https://www.geeksforgeeks.org/group-shifted-string/
https://www.programcreek.com/2014/05/leetcode-group-shifted-strings-java/

Given an array of strings (all lowercase letters), the task is to group them in such a way that all strings in a group
are shifted versions of each other. Two string S and T are called shifted if,

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
class Solution():
    def groupShiftedStrs(self, strs):
        # Tuple Map of Diffs of Char within a str -->
        # Format: {Tuple(diff1, diff2, diff3) : List[str1, str2, str3]}
        # Example: { (2, 1) : ["acd", "dfg", "wyz", "yab", "mop"] } # Each str has same diff!
        m = collections.defaultdict(list)

        # Given a str, calc diff of chars in str. i.e str[1]-str[0] and return a tuple of allDiff i.e (2,1)
        def createTupleKey(s):
            allDiffs = []

            for i in range(1, len(s)):
                oneDiff = ord(s[i]) - ord(s[i-1])
                allDiffs.append(oneDiff)
            return tuple(allDiffs)

        for s in strs:
            key = createTupleKey(s)
            m[key].append(s)        # Append str against SAME diff between chars

        return list(m.values())


strs = ["acd", "dfg", "wyz", "yab", "mop", "bdfh", "a", "x", "moqs"]
print(Solution().groupShiftedStrs(strs))
