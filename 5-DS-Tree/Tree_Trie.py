from re import I


class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.isEndOfWord = False

class TrieTree:
    def __init__(self):
        self.root = TrieNode()

    def __charToIndex__(self, c):
        return ord(c) - ord('a')

    def insert(self, key):
        pCrawl = self.root

        # Example: "lemon"   ----> 
        #       root
        #       /
        #      l
        #     /
        #    e
        #  .... 
        for level in range(len(key)):
            i = self.__charToIndex__(key[level])
            if not pCrawl.children[i]:  # Does not already exists
                pCrawl.children[i] = TrieNode()
            pCrawl = pCrawl.children[i] # Move pointer to that child to insert next char
        pCrawl.isEndOfWord = True   # Mark end of word, so that we know while traversing

    def search(self, key):
        pCrawl = self.root

        for level in range(len(key)):
            i = self.__charToIndex__(key[level])
            if not pCrawl.children[i]:  # One char at this level does not exists... i.e  'l' found but 'e' missing
                return False
            pCrawl = pCrawl.children[i] # 'l' found, move pointer here and search next 'e'

        # Check this is end of word also
        return pCrawl != None and pCrawl.isEndOfWord

    def delete(self, key):
        pCrawl = self.root

        for level in range(len(key)):
            i = self.__charToIndex__(key[level])
            if not pCrawl.children[i]:   # One char at this level does not exists... i.e  'l' found but 'e' missing
                return False
            pCrawl = pCrawl.children[i] # 'l' found, move pointer here and search next 'e'

        # Key exists, but in TRIE nodes could be shared with other keys
        # so make sure it's not before removing
        if pCrawl != None:
            if self.noChildren(pCrawl):
                # node not shared with any other key, safe to delete the key
                del pCrawl
            else:
                # node shared with other key, not safe to delete, just mark non word
                pCrawl.isEndOfWord = False

    def noChildren(self, root):
        for child in self.root.children:
            if child is not None:
                return False
        return True



keys = ["jigar", "krupa", "there", "the"]
myTrie = TrieTree()

for key in keys:
    myTrie.insert(key)

for key in keys:
    print(myTrie.search(key))

print(myTrie.search("ere"))
print(myTrie.search("nothing"))