"""
https://www.geeksforgeeks.org/print-all-possible-paths-from-top-left-to-bottom-right-of-a-mxn-matrix/

Print all possible paths from top left to bottom right of a mXn matrix
The problem is to print all the possible paths from top left to bottom right of a mXn matrix with the constraints that from each cell you can either move only to right or down.

Examples :

Input : 1 2 3
        4 5 6
Output : 1 4 5 6
         1 2 5 6
         1 2 3 6

Input : 1 2
        3 4
Output : 1 2 4
         1 3 4
"""
def printAllMatrixPaths(maze):
    row = 0
    col = 0
    path = []
    return printAllMatrixPaths_Helper(maze, path, row, col)

def printAllMatrixPaths_Helper(maze, path, row, col):
    if row >= rows-1 and col >= cols-1:
        path.append(maze[row][col])
        print(path)
        path.pop()
        path = []

    if row < rows - 1:
        # Still row available
        path.append(maze[row][col])
        printAllMatrixPaths_Helper(maze, path, row + 1, col)
        path.pop()
    if col < cols - 1:
        # Rows exhausted only cols available
        path.append(maze[row][col])
        printAllMatrixPaths_Helper(maze, path, row, col + 1)
        path.pop()


"""
COUNT ALL POSSIBLE PATHS TO REACH FROM START TO END

https://www.geeksforgeeks.org/count-possible-paths-top-left-bottom-right-nxm-matrix/
"""
def countAllMatrixPaths(maze, row, col):
    # BAse Case
    # There is only 1 path to maze[0][0]
    if row == 0 or col == 0:
        return 1

    # Path for this cell, is horizontal + vertical
    return countAllMatrixPaths(maze, row-1, col) + countAllMatrixPaths(maze, row, col-1)

def DP_countAllMatrixPaths(maze):
    # Build result 2D array, that stores MaxNumPath to reach ele [row][col]
    result = [[0 for col in range(cols)] for row in range(rows)]

    for row in range(rows):
        for col in range(cols):
            # First row, First col
            # Only 1 way to reach here, Horizontal OR Vertical
            if row == 0 or col == 0:
                result[row][col] = 1
            else:
                # 2 Ways to reach: Horizontal + Vertical
                result[row][col] = result[row-1][col] + result[row][col-1]
    return result[rows-1][cols-1]

def DP_countAllMatrixPaths_With_Obstacle(input):
    rows = len(input)
    cols = len(input[0])
    # Build result 2D array, that stores MaxNumPath to reach ele [row][col]
    result = [[0 for col in range(cols)] for row in range(rows)]

    for row in range(rows):
        for col in range(cols):
            # First row, First col
            # Only 1 way to reach here, Horizontal OR Vertical
            if row == 0 or col == 0:
                result[row][col] = 1
            elif input[row][col] == 1:
                    result[row][col] = 0
            else:
                # 2 Ways to reach: Horizontal + Vertical
                result[row][col] = result[row-1][col] + result[row][col-1]

    return result[rows-1][cols-1]

"""
TEST Matrix
"""
maze = [[1,2,3],
        [4,5,6],
        [7,8,9]]
rows = len(maze)
cols = len(maze[0])

"""
print "1. All Possible paths from start of matrix to End:"
print "==================================================="
print printAllMatrixPaths(maze)

print "2. Max path to reach from start of matrix to End:"
print "==================================================="
print countAllMatrixPaths(maze, rows-1, cols-1)
"""
print("3. DYnamic-Programming-Max path to reach from start of matrix to End:")
print("=======================================================================")
print(DP_countAllMatrixPaths(maze))


input = [[0,0,0],
        [0,1,0],
        [0,0,0]]
print("3. DYnamic-Programming-With Obstacle")
print("=======================================================================")
print(DP_countAllMatrixPaths_With_Obstacle(input))