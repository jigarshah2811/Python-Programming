def searchMatrix(mat, target):
    rows = len(mat)
    if rows == 0:
        return False
    cols = len(mat[0])

    # Start searching from 1st row, last col
    row, col = 0, cols - 1
    while row < rows and col >= 0:
        if target == mat[row][col]:
            return True
        elif target > mat[row][col]:
            row += 1
        else:
            col -= 1
    return False

def searchMatrix2(mat, target):
    rows = len(mat)
    if rows == 0:
        return False
    cols = len(mat[0])

    # Start searching from 1st row, last col
    row, col = 0, cols - 1
    while row < rows and col >= 0:
        if target == mat[row][col]:
            return True
        elif target > mat[row][col]:
            row += 1
        else:
            col -= 1
    return False

def rotate(mat):
    """
    :type matrix: List[List[int]]
    :rtype: None Do not return anything, modify matrix in-place instead.
    """
    N = len(mat)
    if N == 0:
        return False

    # Outer layers
    for layer in range(0, N/2):
        # Elements in this layer
        first = layer
        last = N-layer-1

        for i in range(first, last):
            rowOffset = N - first - 1
            colOffset = N - i - 1
            # Save Top
            temp = mat[first][i]

            # Left --> Top
            mat[first][i] = mat[colOffset][first]
            # Bottom -> Left
            mat[colOffset][first] = mat[rowOffset][colOffset]
            # Right --> Bottom
            mat[rowOffset][colOffset] = mat[i][rowOffset]
            # Top --> Right
            mat[i][rowOffset] = temp

    return mat

if __name__ == '__main__':
    matrix = [
        [1,2,3,4,5],
        [6,7,8,9,10],
        [11,12,13,14,15],
        [16,17,18,19,20],
        [21,22,23,24,25]
    ]

    print(("Index of 10 in matrix: {0}".format(searchMatrix(matrix, 1))))
    print(("Index of 10 in matrix: {0}".format(searchMatrix(matrix, 25))))
    print(("Index of 10 in matrix: {0}".format(searchMatrix(matrix, 10))))
    print(("Index of 10 in matrix: {0}".format(searchMatrix(matrix, 18))))
    print(("Index of 10 in matrix: {0}".format(searchMatrix(matrix, 50))))

    # Boundry conditions
    print(("Empty matrix: {0}".format(searchMatrix([], 1))))

    # Matrix II
    matrix = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]
    print(("Index of 10 in matrix: {0}".format(searchMatrix(matrix, 9))))
    print(("Index of 10 in matrix: {0}".format(searchMatrix(matrix, 21))))
    print(("Index of 10 in matrix: {0}".format(searchMatrix(matrix, 20))))



    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    print("Rotated Matrix")
    print((rotate(matrix)))