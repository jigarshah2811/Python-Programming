class Solution:
    def solveSudoku(self, board):
        def isValidSudoku(self, board, row, col, num):
            bigSet = set()

            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j] != 0:
                        cur = board[i][j]
                        # Check for duplicate in ROW/COL/BOX through a set!
                        if (i, cur) in bigSet or (cur, j) in bigSet or (i / 3, j / 3, cur) in bigSet:
                            return False
                        bigSet.add((i, cur))  # Add rows values in set
                        bigSet.add((cur, j))  # Add cols values in set
                        bigSet.add((i / 3, j / 3, cur))  # Add box values in set
            return True

        def getNextEmptyCell():
            for row in range(rows):
                for col in range(cols):
                    if board[row][col] == '.':
                        return (row, col)
            return -1, -1

        def isSafe(row, col, ch):
            boxrow = row - row % 3
            boxcol = col - col % 3
            if checkrow(row, ch) and checkcol(col, ch) and checksquare(boxrow, boxcol, ch):
                return True
            return False

        def checkrow(row, ch):
            for col in range(9):
                if board[row][col] == ch:
                    return False
            return True

        def checkcol(col, ch):
            for row in range(9):
                if board[row][col] == ch:
                    return False
            return True

        def checksquare(row, col, ch):
            for r in range(row, row + 3):
                for c in range(col, col + 3):
                    if board[r][c] == ch:
                        return False
            return True

        def backtrack():
            # 1) Base case
            (row, col) = getNextEmptyCell()
            if row == -1 and col == -1:
                return True

            # 2) Breath
            for val in map(str, list(range(1, 10))):
                # 3) IsSafe
                if isSafe(row, col, val):
                    # 4) Apply this val to cell
                    board[row][col] = val
                    # 5) Depth: Backtrack for next cell
                    if backtrack():
                        return True
                    # 6) Backtrack
                    board[row][col] = '.'

            return False

        rows, cols = len(board), len(board[0])
        backtrack()
        return board


s = Solution()
board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]
print((s.solveSudoku(board)))
