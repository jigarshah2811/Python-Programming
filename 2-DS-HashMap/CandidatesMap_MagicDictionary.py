import collections

class MagicDictionary:
    def __init__(self) -> None:
        self.md = collections.defaultdict(str)
    
    def addWord(self, word):
        self.md[word] = True
        word = list(word)
        for i, _ in enumerate(word):
            wildCardWord = word
            wildCardWord[i] = "*"
            self.md[str(wildCardWord)] = True

    def addWords(self, words):
        for word in words:
            self.addWord(word)
    
    def searchWord(self, word):
        if self.md[word]:
            return True
            
        word = list(word)
        for i, _ in enumerate(word):
            wildCardWord = word
            wildCardWord[i] = "*"
            if str(wildCardWord) in self.md:
                return True
        
        return False
    
magicDict = MagicDictionary()
words = ["apple", "code"]
magicDict.addWords(words)
print(magicDict.searchWord("apple"))    # True Explanation: self word
print(magicDict.searchWord("apply"))   # True  Explaination: apple will have appl* that matches with apply
print(magicDict.searchWord("lode"))    # True  Explanation:  code will have  *ode  that matches with lode
print(magicDict.searchWord("god"))     # False