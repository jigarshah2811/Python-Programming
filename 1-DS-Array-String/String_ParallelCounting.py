""" DS: Map         Pattern: String Counting """

from collections import defaultdict
class Solution:
    def minNumberOfFrogs(self, text: str) -> int:
        # Freq Map: {char: count}
        seen = defaultdict(int)     
        
        # At each char, check if the string is still valid
        # Example: croakcrook {c: 2, o: 3} --> marks text invalid because o is more then c!
        def isValid(c):
            seen[c] += 1
            if seen['c'] >= seen['r'] >= seen['o'] >= seen['a'] >= seen['k']:
                return True
            else:
                return False
        
        
        # Go through text, Increase frog on 'c', Decrease on 'k', Check validity on all others
        frogs, maxFrogs = 0, 0
        
        for i, c in enumerate(text):
            if not isValid(c):
                return -1
            
            match c:
                case 'c':                    
                    frogs += 1   # Frog started croacking, new frog
                case 'k':
                    frogs -= 1   # Frog finished croacking, can be re-used
                
            maxFrogs = max(maxFrogs, frogs)
                    
        # Edge case: Example: "croa"
        if frogs == 0:  # All croacking is complete?
            return maxFrogs
        else:
            return -1