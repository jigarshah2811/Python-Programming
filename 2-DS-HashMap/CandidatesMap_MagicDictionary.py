import collections
class MagicDictionary(object):
    def __init__(self):
        self.mySet = set()
        self.myDict = dict()

    def _candidates(self, word):
        for i in range(len(word)-1):
            candidate = word[:i] + "*" + word[i+1:]
            print(candidate)
            yield candidate

    def buildDict(self, words):
        for word in words:
            self.mySet.add(word)
            for cand in self._candidates(word):
                try:
                    self.myDict[cand] += 1
                except:
                    self.myDict[cand] = 1

    def search(self, word):
        for cand in self._candidates(word):
            if cand in self.myDict:
                count = self.myDict[cand]
                any (count > 1 or
                    count == 1 and word not in self.mySet)
        return False


md = MagicDictionary()
md.buildDict(["apple, leetcode"])
print(md.search("apply"))

"""
md.buildDict(["apple, apply, leetcode"])
print md.search("apply")
md.buildDict(["hello, leetcode"])
print md.search("yello")
"""