import collections
from typing import List

"""
A Trie is combination of A-Z children node (as keys) with each having values = TrieNode (A-Z children node)
   root (TrieNode)
   ---------------
   a        b       .......
   |        |
TrieNode TrieNode
a .... z a......z
   
"""
class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isWord = False         # Weather there is a Word ending here at this node

class TrieTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for c in word:
            if c in node.children:          # char Node already exists, just crawl through
                node = node.children[c]
            else:
                node.children[c] = TrieNode() # char Node does not exists, create one and crawl through
                node = node.children[c]
        node.isWord = True                     # Mark this word=True, since there's a word available in Trie node

    def find(self, word):
        node = self.root
        for c in word:
            if c not in node.children:      # Keep crawling through children since char in word exists...
                return False                # Char is missing so this word is incomplete, does not exists
        return node.isWord


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        def isSafe(row, col, node): # Essure, we are within the board (row, col) AND TrieNode is valid boundary no OOB
            if (0 <= row < rows) and (0 <= col < cols) and (node is not None):
                return True
            return False

        def backtrack(row, col, node, res):
            # 1) Base case, if a word is found in matrix. Add sol in finalResult
            if node is None:
                return
            if node.isWord:                 # We hit in TrieTree a word, so that's found in our board
                finalResult.append(res)     # store sol in finalResult
                node.isWord = False         # Avoid finding this word again....

            # 2) Breath ---> Look for this word in all directions --> <--- upar and niche
            # 3) isSafe
            if isSafe(row, col, node):
                # 4) Take this move
                tmp = board[row][col]
                res += tmp
                board[row][col] = '#'   # Mark this char visited so does not visit again

                # 5) Breath ---> Try all possible directions ---> <--- upar niche.
                # Depth .---> For the next char of the currently searched word
                node = node.children.get(tmp)
                res = backtrack(row+1, col, node, res) or backtrack(row-1, col, node, res) or \
                      backtrack(row, col+1, node, res) or backtrack(row, col-1, node, res)

                # 6) Backtrack
                board[row][col] = tmp   # No combination -> <- upar niche found this word. So revert back original va;

            return False

        finalResult = []
        # Creating a TRIE tree to easily search word char-by-char
        trie = TrieTree()
        node = trie.root
        for word in words:
            trie.insert(word)       # Create Trie with all given words. Use it in DFS to search a word

        # Search for a word from every point of matrix
        rows, cols = len(board), len(board[0])
        for row in range(rows):
            for col in range(cols):
                backtrack(row, col, node, res="")

        return finalResult


s = Solution()
board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]
print((s.findWords(board, words)))