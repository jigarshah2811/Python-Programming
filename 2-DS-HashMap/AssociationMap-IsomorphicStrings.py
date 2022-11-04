"""
DS: Associative Map   d{sChar: tChar}  # meaning of sChar in S is equivalent to tChar in T

https://leetcode.com/problems/isomorphic-strings/submissions/
Pattern:    {sChar --> CommonVal <---  tChar}
Pattern:    {sChar --> tChar} AND {tChar ---> sChar}

https://leetcode.com/problems/linked-list-random-node/
Pattern:    {oldNode: newNode}
Algorithm:  newNode.next = NewMap[oldNode.next], newNode.random = NewMap[oldNode.random]

https://leetcode.com/problems/clone-graph/
Pattern:    {oldNode: newNode}
Algorithm:  newNode.Conn = NewMap[oldNode.Conn]     for all conns!

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

    """DS: Bi-Directional Map
    Sorce ---> maps to expected Target
    Target --> maps to expected Source

    Old maps to New AND New maps to Old values!
    """
    def isIsomorphicTwoMaps(self, S: str, T: str) -> bool:
        sMap, tMap = defaultdict(str), defaultdict(str)

        for s, t in zip(S, T):
            # A key is seen! Verify it maps to the right val (Dest Key!)
            if s in sMap or t in tMap:
                if sMap[s] != t or tMap[t] != s:
                    return False
            
            # A key is NOT seen, Store Association from s --> t char!
            sMap[s] = t
            tMap[t] = s

        return True


solution = Solution()

s = "egg"; t = "add"
print(solution.isIsomorphicTwoMaps(s, t)) # Expected True

s = "foo"; t = "bar"
print(solution.isIsomorphicTwoMaps(s, t)) # Expected False

s = "paper"; t = "title"
print(solution.isIsomorphicTwoMaps(s, t)) # Expected True

