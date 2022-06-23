"""
https://leetcode.com/problems/shortest-word-distance/solution/
"""
import collections
class WordDistanceFinder(object):

    def __init__(self, words):
        self.words = words
    

    """
    Find word1 and word2, calculate distance
    Find next occurance of word1 OR word2, calculate distance again
    Keep track of minimum distance
    """
    def wd(self, word1, word2):
        # Keep track of running minimum distance, while found dist each time
        minDist = float("inf")
        # Keep track of index for word1 and word2
        pos1 = None
        pos2 = None

        # Keep looking for occurance of word1 or word2 and calc distance each time
        for i in range(len(words)):
          if self.words[i] == word1:
              pos1 = i
          if self.words[i] == word2:
              pos2 = i

          # New index for word1 or word2 found, calculate distance
          if pos1 is not None and pos2 is not None:
              minDistTillNow = abs(pos1 - pos2)
              # keep track of minimum distance till now
              minDist = min(minDist, minDistTillNow)

        return minDist

"""
Build Frequency list map to be able to find distance between any given 2 words
{word1: [index1, index2, ...]
 word2: [index1, index2, ...]}
"""
class WordDistance(object):
    def __init__(self, words):
        self.d = collections.defaultdict(list)
        for i, word in enumerate(words): # IndexMap { Word --> List[index1, index2] }
            self.d[word].append(i)

    def wd(self, word1, word2):
        # Get indexes word1 is seen and word2 is seen
        l1 = self.d[word1]
        l2 = self.d[word2]

        # Edge case, when both words are same! { 'fox' --> [1, 5, 6]  should return minDistance=1}
        minDistance = float('inf')
        if word1 == word2:
            if len(l1) == 1:
                return 0
            else:
                for j in range(1, len(l1)):
                    minDistance = min(minDistance, (l1[j] - l2[j-1]))
            return minDistance

        # l1 and l2 are already SORTED list. Do a Merge to find out minDistance between i and j
        i, j = 0, 0
        while i < len(l1) and j < len(l2):
            curDist = abs(l1[i] - l2[j])
            minDistance = min(minDistance, curDist)
            # Move the min index
            if l1[i] < l2[j]:
                i += 1
            else:
                j += 1

        return minDistance


words = ["practice", "makes", "perfect", "coding", "makes"]
word1, word2 = "coding", "makes"

twoPointerSol = WordDistanceFinder(words)
print((twoPointerSol.wd(word1, word2)))

indexMapSol = WordDistance(words)
print((indexMapSol.wd(word1, word2)))
print((indexMapSol.wd(word1, word1)))


