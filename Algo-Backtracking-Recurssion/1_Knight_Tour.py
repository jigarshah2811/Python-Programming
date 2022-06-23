"""
Template for Backtracking solution

See Steps 1) to 6) are the main steps to follow for any backtracking solution trying all comb within a constraint

Permutations: For backtracking sol to use against permute problems, just remove isSafe! Since every comb is valid!
"""

"""
https://www.geeksforgeeks.org/the-knights-tour-problem-backtracking-1/

"""

class Solution:
    def knightTour(self, N):
        def isSafe(x, y):
            # Check cell (x, y) is not OOB and value is not visited already
            if 0 <= x < N and 0 <= y < N and board[x][y] == -1:
                return True
            return False

        def backtrack(cur_x, cur_y, moveCount):
            # 1) Base case: If all moves are done
            if moveCount >= N*N:
                return True

            # 2) Breath: --> Consider all possible moves
            for i in range(8):
                next_x = cur_x + move_x[i]
                next_y = cur_y + move_y[i]

                # 3) Check if this move can be taken
                if isSafe(next_x, next_y):
                    # 4) Take this move
                    board[next_x][next_y] = moveCount

                    # 5) Check if this move leads to a solution from all recur moves
                    if backtrack(next_x, next_y, moveCount+1):
                        return True

                    # 6) This move didn't work, Backtrack...
                    board[next_x][next_y] = -1

            return False    # No move from all 8 possible worked, so Backtrack previous move and re-try

        # Initialize NxN chess board
        board = [[-1 for i in range(N)] for j in range(N)]

        # Possible moves of a knight on chess-board, X and Y coordinates
        move_x = [2, 1, -1, -2, -2, -1, 1, 2]
        move_y = [1, 2, 2, 1, -1, -2, -2, -1]

        board[0][0] = 0         # start with the Knight is initially at the first block
        backtrack(0, 0, 1)      # Step counter for knight's position
        return board


s = Solution()
print((s.knightTour(8)))
