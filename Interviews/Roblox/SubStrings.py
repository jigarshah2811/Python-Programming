import collections
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        
        def isWordSubString(word):
            q = collections.deque(s)
            # print(f"Starting with, Queue: {q}, word: {word}")

            i = 0

            while q:
                if q.popleft() == word[i]:
                    i += 1
                    if i >= len(word):  # Bingo entire word matchd already                        
                        return 1
            
            
            # print(f"Ending with, Q: {q}, word: {word[i:]}")
            # Q is empty now
            return 0
        
        
        return sum(map(isWordSubString, words))
