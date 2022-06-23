"""
https://leetcode.com/problems/isomorphic-strings/submissions/
"""
"""
https://leetcode.com/problems/linked-list-random-node/
"""

from collections import defaultdict


class Solution:
    def isIsomorphic(self, S: str, T: str) -> bool:
        commonMap = defaultdict(int)
        
        count = 0
        # Build commonMap, while looking for anomoly
        for s, t in zip(S, T):
            # Both values are missing in map, create a common count for them
            if s not in commonMap and t not in commonMap:
                commonMap[s] = count
                commonMap[t] = count
                count += 1
            # One exists but other does not exists in map
            elif commonMap[s] and not commonMap[t]:
                commonMap[t] = commonMap[s]
            elif commonMap[t] and not commonMap[s]:
                commonMap[s] = commonMap[t]
            # Both exists, check they refer to the same common count, otherwise it's anomoly
            elif commonMap[s] != commonMap[t]:
                    return False
            else:
                # Both chars are present and refers to the common count! Keep going...
                continue
        
        print(commonMap)
        return True

    def isIsomorphicTwoMaps(self, S: str, T: str) -> bool:
        sMap, tMap = defaultdict(int), defaultdict(int)
        for s, t in zip(S, T):
            if (s in sMap and sMap[s] != t) or (t in tMap and tMap[t] != s):
                return False
            sMap[s] = t
            tMap[t] = s
        
        print(sMap, tMap)
        return True

solution = Solution()

s = "egg"; t = "add"
print(solution.isIsomorphicTwoMaps(s, t)) # Expected True

s = "foo"; t = "bar"
print(solution.isIsomorphicTwoMaps(s, t)) # Expected False

s = "paper"; t = "title"
print(solution.isIsomorphicTwoMaps(s, t)) # Expected True
