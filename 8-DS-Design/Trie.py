class TrieNode:
    def __init__(self):
        self.children = {}  # {char -> TrieNode (Subtree)}
        self.isEndOfWord = False
        self.sug = []


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, product):
        crawl = self.root
        for c in product:
            if c not in crawl.children:
                crawl.children[c] = TrieNode()

            # Crawl down for next char
            crawl = crawl.children[c]
            # Suggestion at each level
            if len(crawl.sug) < 3:
                crawl.sug.append(product)

        crawl.isEndOfWord = True

    def search(self, searchWord):
        ans = []
        crawl = self.root
        for c in searchWord:
            if crawl:
                crawl = crawl.children.get(c, None)
            ans.append(crawl.sug if crawl else [])

        return ans

""" Google Search Suggestions while typing each Char!!! (Autofill system)
https://leetcode.com/problems/search-suggestions-system/submissions/
"""
class Solution:
    def suggestedProducts(self, products, searchWord):
        root = Trie()
        for product in sorted(products):
            root.insert(product)

        ans = root.search(searchWord)
        return ans




s = Solution()
products = ["mobile","mouse","moneypot","monitor","mousepad"]
searchWord = "mouse"
print(s.suggestedProducts(products, searchWord))