"""
Q: How many horses are there a string with multiple ‘neighs’ in it; Given a string (of horse sound ‘neigh’), 
determine the minimum number of horses possible. ‘Nneigheigh’ should return 2, ‘neighneigh’ returns 1.
"""

import collections
from ctypes.wintypes import HMODULE
from nis import match
import string


class Solution:
    def __init__(self) -> None:
        pass
        
    # counts how many horses are singing in PARALLEL and returns #of horses
    def countHorses(self, text: str) -> int:
        freq = collections.defaultdict(int) # Map {char: freq}  
        def isValid(c):
            freq[c] += 1
            if freq['n'] >= freq['e'] >= freq['i'] >= freq['g'] >= freq['h']:
                return True
            return False
        
        
        horses, maxHorses = 0, 0
        for c in text.lower():
            if not isValid(c):      # Invalid string, for example: more 'e' then 'n' or so
                return 0
            match c:
                case 'n':
                    horses += 1
                    maxHorses = max(maxHorses, horses)
                case 'h':
                    horses -= 1
    
        return maxHorses
        

        


s = Solution()
assert(s.countHorses("neigh") == 1)
assert(s.countHorses("neighneigh") == 1)      # same horse finished 'neight', spoke another 'neigh'
assert(s.countHorses("Nneigheigh") == 2)      # 'n' is starting in middle of one 'neigh'
assert(s.countHorses("Nneighneigheigh") == 2)      # 'n' is starting in middle of one 'neigh'
assert(s.countHorses("NneigNheigheigh") == 3)      # 'n' is starting in middle of one 'neigh'
assert(s.countHorses("Nneigheih") == 0)      # 'g' missing from one 'neigh'