import collections


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        sMap = tMap = [0] * 256         # SAME POINTER!!
        # tMap = [0]*256                # DIFF MAPS
        count = 0

        for i in range(len(s)):

            if sMap[ord(s[i])] != tMap[ord(t[i])]:
                print((i, sMap[ord(s[i])], tMap[ord(t[i])]))

                return False
            sMap[ord(s[i])] = i + 1
            tMap[ord(t[i])] = i + 1

        return True