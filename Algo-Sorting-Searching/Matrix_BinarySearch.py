class Solution:
    def searchMatrix(self, matrix, target):
        # Edge cases
        rows = len(matrix)
        if rows == 0:
            return False
        cols = len(matrix[0])

        row, col = 0, cols - 1
        while row < rows and col >= 0:
            if matrix[row][col] == target:
                return True  # Found
            elif matrix[row][col] < target:  # eliminate row
                row += 1
            else:  # eliminate col
                col -= 1

        return False  # Not found


s = Solution()
matrix = [[1]]
print((s.searchMatrix(matrix, 1)))
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
print((s.searchMatrix(matrix, 16)))
print((s.searchMatrix(matrix, 3)))
