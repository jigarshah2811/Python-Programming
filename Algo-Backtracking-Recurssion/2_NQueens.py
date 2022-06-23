class Solution:
    def solveNQueens(self, n):
        def isSafe(row, col):
            if (col in queens) or (row - col in xy_diff) or (row + col in xy_sum):
                return False
            return True

        def backtrack(row):
            # 1) Base case: If we reach to solution, store it
            if row >= n:  # Found 1 solution
                result.append(queens[:])
                return True

            # 2) Breath --> For all cols in this row
            for col in range(n):
                # 3) Check if this move is safe
                if isSafe(row, col):
                    # 4) Take this move
                    print(("Placing queen at: ({0}, {1})".format(row, col)))
                    sol[row][col] = 1
                    queens.append(col), xy_sum.append(row + col), xy_diff.append(row - col) # Mark col, diag danger!

                    # 5) Recursively check if we can reach sol, place queen to next row
                    backtrack(row + 1)

                    # 6) Backtrack
                    print(("Backtracking queen from: ({0}, {1})".format(row, col)))
                    sol[row][col] = 0
                    queens.remove(col), xy_sum.remove(row + col), xy_diff.remove(row - col) # Mark col, diag safe!

        result = []
        queens, xy_diff, xy_sum = [], [], []
        sol = [[0] * n] * n
        backtrack(0)
        return [["." * i + "Q" + "." * (n - i - 1) for i in sol] for sol in result]     # Convert in beautiful format to see where Q are placed


s = Solution()
print((s.solveNQueens(4)))
