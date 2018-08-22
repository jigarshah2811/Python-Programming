# Possible knight moves
moveX = [2, 1, -1, -2, -2, -1,  1,  2]
moveY = [1, 2,  2,  1, -1, -2, -2, -1]
N = 8  # 8 X 8 Chess Board
src_x, src_y = 0, 0
dest_x, dest_y = 4, 3


def solveKT():
    global moveX
    global moveY
    global N

    # Initialize the N*N Chess board with no solution
    sol = [[-1] * N for i in xrange(N)]

    # Start from (0,0) location
    x, y = 0, 0
    moveCount = 1
    sol[x][y] = 0
    result, sol = solveKT_Helper_AllMoves(x, y, sol, moveCount)
    if result:
        print sol
    else:
        return False


def solveKT_SrcToDest():
    global moveX
    global moveY
    global N
    global src_x
    global src_y
    global dest_x
    global dest_y

    # Initialize the N*N Chess board with no solution
    sol = [[-1] * N for i in xrange(N)]

    # Start from (0,0) location
    moveCount = 1
    sol[src_x][src_y] = 0
    result, totalWays = solveKT_Helper_SrcToDest(src_x, src_y, sol, moveCount, 0)
    if result:
        print totalWays
    else:
        return False


def isSafe(x, y, sol):
    if 0 <= x < N and 0 <= y < N and sol[x][y] == -1:
        return True


def solveKT_Helper_AllMoves(x, y, sol, moveCount):
    global moveX
    global moveY
    global N

    """
    BACKTRACKING PATTERN
    """
    # 1) Base Case
    # All moves are covered
    if moveCount == N*N:
        return True, sol

    # 2) BFS ---> Generate all possible moves
    for i in xrange(len(moveX)):
        next_x = x + moveX[i]
        next_y = y + moveY[i]

        # 3) Is the move valid ?
        if isSafe(next_x, next_y, sol):

            # 4) Take next move
            sol[next_x][next_y] = 0

            # 5) DFS --> Recursively check if this move leads to sol
            if solveKT_Helper_AllMoves(next_x, next_y, sol, moveCount + 1):
                return True, sol

            else: # 6) Else backTrack the move
                sol[next_x][next_y] = -1


def solveKT_Helper_SrcToDest(x, y, sol, moveCount, totalWays):
    global moveX
    global moveY
    global N
    global dest_x
    global dest_y

    """
    BACKTRACKING PATTERN
    """
    # 1) Base Case
    # If Src knight reaches to dest knight pos
    if x == dest_x and y == dest_y:
        totalWays += 1
        print "               TotalWays: {0}, MoveCount: {1}".format(totalWays, moveCount)
        return True, totalWays

    # 2) BFS ---> Generate all possible moves
    for i in xrange(len(moveX)):
        next_x = x + moveX[i]
        next_y = y + moveY[i]

        # 3) Is the move valid ?
        if isSafe(next_x, next_y, sol):

            # 4) Take next move
            sol[next_x][next_y] = 0

            # 5) DFS --> Recursively check if this move leads to sol
            result, totalWays = solveKT_Helper_SrcToDest(next_x, next_y, sol, moveCount + 1, totalWays)

            # 6) Else backTrack the move
            sol[next_x][next_y] = -1

    return True, totalWays


def main():
    print solveKT()
    print solveKT_SrcToDest()

if __name__ == "__main__":
    main()