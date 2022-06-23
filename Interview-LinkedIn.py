"""
         root
      /       \
    a     |     a
   / \    |    / \
  b   c   |   c   b
 / \      |      / \
d   e     |      e  d    return true

         root
      /       \
    a     |     a
   / \    |    / \
  b   c   |   c   c
 / \      |      / \
d   e     |      e  d    return false

struct Node {
  int data;
  Node *left;
  Node *right; 
} Node;

bool isSelfMirrorTree(root) {
  return true or false;
}
"""
def isMirror(src, dest):
    # Validations
    # If both are none, return True
    if src is None and dest is None:
        return True
    
    if src is None or dest is None:
        return False

    # 1) Root matches
    # 2) Constraint for L & R Subtree matches
    return src.data == dest.data and isMirror(src.left, dest.right) and isMirror(src.right, dest.left)

def isSelfMirrorTree(root):
    # Empty tree is mirro
    if root is None:
        return True
    return isMirror(root.right, root.left)

    
# time complexity is O(log n) is O(n)

# * This class will be given a list of words (such as might be tokenized
# * from a paragraph of text), and will provide a method that takes two
# * words and returns the shortest distance (in words) between those two
# * words in the provided text.
# * Example:
# *   WordDistanceFinder finder = new WordDistanceFinder(Arrays.asList("the", "quick", "brown", "fox", "quick"));
# *   assert(finder.distance("fox", "the") == 3);
# *   assert(finder.distance("quick", "fox") == 1);
# *
# * "quick" appears twice in the input. There are two possible distance values for "quick" and "fox":
# *     (3 - 1) = 2 and (4 - 3) = 1.
# * Since we have to return the shortest distance between the two words we return 1.

import math
class WordDistanceFinder(object):

    def __init__(self, words):
        self.words = words
        
    def wd(self, word1, word2):
        # locals
        retVal = 65535
        pos1 = None
        pos2 = None

        for i in xrange(len(words)):
          if self.words[i] == word1:
              pos1 = i
          if self.words[i] == word2:
              pos2 = i

          # GEt min
          if pos1 is not None and pos2 is not None:
              retVal = min(retVal, abs(pos1 - pos2))

        return retVal

# tests
words = ["the", "quick", "brown", "fox", ""]
obj = WordDistanceFinder(words)
print obj.wd("the", "quick")
print obj.wd("the", "fox")

"""
# Optimized version
class WordDistanceFinderOptimized(object):

    def __init__(self, words):
        self.words = words
        self.d = dict()
        self.storeInDict()

    def storeInDict(self):
        for i in xrange(len(words)):
            try:
                self.d[words[i]].append(i)
            except KeyError:
                self.d[words[i]] = [i]
     
    def wd(self, word1, word2):
        retVal = 65535
        pos1 = None
        pos2 = None

        if word1 in self.d:
          pos1 = self.d[word1]
        if word2 in self.d:
          pos2 = self.d[word2]

        # GEt min
        retVal = min(retVal, min(min(pos1), min(pos2)), max(max(pos1), max(pos2)))

        return retVal
"""
# O(N)
words = ["the", "quick", "brown", "fox", "the"]
obj = WordDistanceFinder(words)
print obj.wd("the", "quick")
print obj.wd("the", "fox")

"""
# O(log(pos)) binary search to find min delta between 2 lists of positions. 
a: 1,2,3
b: 4,5,6
"""
