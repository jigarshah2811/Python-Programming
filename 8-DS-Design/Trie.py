class TrieNode:
    def __init__(self):
        self.children = {}  # {char -> TrieNode (Subtree)}  Example: {'t': TrieNode()}
        self.isEndOfWord = False
        self.sug = []


""" Google Search Suggestions while typing each Char!!! (Autofill system)
https://leetcode.com/problems/search-suggestions-system/submissions/
"""
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        crawl = self.root   # Start from root and keep adding each char in height of tree
        for c in word:
            if c not in crawl.children: # If this char not already a child then make one
                crawl.children[c] = TrieNode()

            # Crawl down for next char  ---> Keep moving down
            crawl = crawl.children[c]   # value of this 'c' in map is the TrieNode (child node)
            
            # Store this char as Suggestion at each level   Example: "Parro." 't' will follow
            if len(crawl.sug) < 3:
                crawl.sug.append(word)
        
        # mark last node as leaf
        crawl.isEndOfWord = True    # Mark end of word 

    def insertWords(self, words):
        for word in words:
            self.insert(word)

    def searchWord(self, word):
        crawl = self.root
        for c in word:
            if c in crawl.children:
                crawl = crawl.children[c]
            else:
                print(f"{c} does not exists while searching for {word}")
                return False
        
        return crawl.isEndOfWord

    # Find auto-suggestions for targetted word
    def searchSuggestions(self, searchWord):
        ans = []
        crawl = self.root   # Always start from root to crawl
        for c in searchWord:   
            if crawl: # the child exists
                crawl = crawl.children.get(c, None)
            ans.append(crawl.sug if crawl else [])

        return ans

trie = Trie()
words = ["parrot", "mobile","mouse","monitor","mousepad"]
trie.insertWords(words)


print(trie.searchWord("parrot"))        # present
print(trie.searchWord("mouse"))         # present
print(trie.searchWord("patrot"))        # not present

print(trie.searchSuggestions("mouse"))      # Auto suggestion as you type 'm' then 'o' then 'u'.....
print(trie.searchSuggestions("mousepad"))  # Auto suggestion as you type 'm' then 'o' then 'u'.....