"""
http://www.geeksforgeeks.org/print-a-given-matrix-in-spiral-form/

Print a given matrix in spiral form
Given a 2D array, print it in spiral form. See the following examples.

Input:
        1    2   3   4
        5    6   7   8
        9   10  11  12
        13  14  15  16
Output:
1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10


Input:
        1   2   3   4  5   6
        7   8   9  10  11  12
        13  14  15 16  17  18
Output:
1 2 3 4 5 6 12 18 17 16 15 14 13 7 8 9 10 11
spiral-matrix
"""


def spiralOrder(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[int]
    """
    resMat = []

    first_row, first_col = 0, 0
    last_row = len(matrix)-1
    if last_row <= 0:
        return False
    last_col = len(matrix[0])-1

    while True:
        # First ROW, use colIndex++
        for colIndex in range(first_col, last_col+1):
            resMat.append(matrix[first_row][colIndex])

            # eliminate
        first_row += 1
        if first_row >= last_row:
            break

        # Last Col, use rowIndex++
        for rowIndex in range(first_row, last_row+1):
            resMat.append(matrix[rowIndex][last_col])

            # eliminate
        last_col -= 1
        if last_col < first_col:
            break

        # Last ROW, use colIndex--
        for colIndex in reversed(range(first_col, last_col+1)):
            resMat.append(matrix[last_row][colIndex])

        last_row -= 1
        if last_row < first_row:
            break

        # First Col, use rowIndex--
        for rowIndex in reversed(range(first_row, last_row+1)):
            resMat.append(matrix[rowIndex][first_col])

            # eliminate
        first_col += 1
        if first_col >= last_col:
            break

    return resMat

def print_spiral(matrix):
    '''matrix is a list of list -- a 2-d matrix.'''
    first_row = 0
    last_row = len(matrix) - 1
    first_column = 0
    last_column = len(matrix[0]) - 1

    while True:
        # Print first row
        for col_idx in range(first_column, last_column + 1):
            print((matrix[first_row][col_idx]))

        first_row += 1
        if first_row > last_row:
            return

        # Print last column
        for row_idx in range(first_row, last_row + 1):
            print((matrix[row_idx][last_column]))

        last_column -= 1
        if last_column < first_column:
            return

        # Print last row, in reverse
        for col_idx in reversed(list(range(first_column, last_column + 1))):
            print((matrix[last_row][col_idx]))

        last_row -= 1
        if last_row < first_row:
            return

        # Print first column, bottom to top
        for row_idx in reversed(list(range(first_row, last_row + 1))):
            print((matrix[row_idx][first_column]))

        first_column += 1
        if first_column > last_column:
            return

if __name__ == '__main__':
    mat = [[1,2,3,4],
           [5,6,7,8],
           [9,10,11,12],
           [13,14,15,16]]
    #print_spiral(mat)

    mat = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
    print((spiralOrder(mat)))

    mat = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]

    #print_spiral(mat)

    print((spiralOrder(mat)))