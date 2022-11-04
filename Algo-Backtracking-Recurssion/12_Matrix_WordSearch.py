from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def isSafe(row, col, index):
            if 0 <= row < rows and 0 <= col < cols and board[row][col] == word[index]:
                return True
            return False

        def backtrack(row, col, index):
            if index == len(word):      # Word is found
                return True

            # 2) Breath... --> <-- Niche Upar

            if isSafe(row, col, index):
                savedChar = board[row][col]
                board[row][col] = "#"       # Avoid visiting same cell again

                result = backtrack(row + 1, col, index + 1) or backtrack(row, col + 1, index + 1) \
                         or backtrack(row - 1, col, index + 1) or backtrack(row, col - 1, index + 1)

                board[row][col] = savedChar

                return result

        rows, cols = len(board), len(board[0])
        for row in range(rows):
            for col in range(cols):
                if backtrack(row=row, col=col, index=0):
                    return True

        return False


s = Solution()
board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
print((s.exist(board, "ABCCED")))
print((s.exist(board, "SEE")))
print((s.exist(board, "ABCB")))

board = [["C","A","A"],["A","A","A"],["B","C","D"]]
print((s.exist(board, "AAB")))
