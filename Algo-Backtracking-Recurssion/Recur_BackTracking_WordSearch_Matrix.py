class Solution(object):
    def exist(self, board, word):
        ###### BACKTRACKING ##########

        # 1) Breath -->: Go through all cells in matrix
        for i in range(len(board)):
            for j in range(len(board[0])):

                # 2) isSafe --> Constraint: Word char match
                # 3) Depth --->
                if self.DFS(board, word, i, j):
                    # All word char matched from this cell
                    return True

        return False

    def DFS(self, board, word, i, j):
        # Base case
        if len(word) == 0:
            # Everything from the word matched
            return True

        # 2) isSafe --> # OOB
        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]):
            # print "OOB {0}{1}".format(i,j)
            return False

        # Constraint: word char should match to this cell
        if board[i][j] != word[0]:
            # print "Don't match {0}{1}".format(i,j)
            return False
        # Most Imp DFS thing: Mark the cell visited to prevent visiting again!!!
        # 4) BackTracking
        # 4.1) Take a move
        tmp = board[i][j]
        board[i][j] = "#"

        # 4.2) See if recursively lead to solution
        res = self.DFS(board, word[1:], i, j + 1) or \
              self.DFS(board, word[1:], i, j - 1) or \
              self.DFS(board, word[1:], i - 1, j) or \
              self.DFS(board, word[1:], i + 1, j)

        # 4.3) Backtrack
        board[i][j] = tmp
        return res


board =[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
s = Solution()
print(s.exist(board, "ABCCED"))
print(s.exist(board, "SEE"))
print(s.exist(board, "ABCB"))

board = [["a"]]
print(s.exist(board, "a"))