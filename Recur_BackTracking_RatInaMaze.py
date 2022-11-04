N = 4


def isSafeMove(maze, row, col):
    global N

    if row > N-1 or col > N-1 or maze[row][col] == 0:
        return False
    else:
        return True


def solveMazeHelper(maze, sol, row, col):
    global N

    # Base Case
    if row == N-1 and col == N-1:
        if maze[row][col] == 1:
            return True
        else:
            return False

    if isSafeMove(maze, row, col):
        # 1) Take the move
        sol[row][col] = 1

        # 2) See if Recursively leads to sol
        if solveMazeHelper(maze, sol, row + 1, col):
            return True

        if solveMazeHelper(maze, sol, row, col + 1):
            return True

        # 3) Else BackTrack the move
        sol[row][col] = 0
        return False
    return False


def solveMaze(maze):
    global N

    sol = [[-1]*N for i in xrange(N)]
    x, y = 0, 0
    sol[x][y] = 1
    return solveMazeHelper(maze, sol, x, y)


maze = [[1, 0, 0, 0],
        [1, 1, 0, 1],
        [0, 1, 0, 0],
        [1, 1, 1, 0]
        ]
print solveMaze(maze)
