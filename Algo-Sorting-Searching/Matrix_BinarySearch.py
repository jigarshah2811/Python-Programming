class Solution:
    def searchMatrix(self, matrix, target):
        # Edge cases
        rows = len(matrix)
        if rows == 0:
            return False
        cols = len(matrix[0])

        row, col = 0, cols - 1
        while row < rows and col >= 0:
            if matrix[row][col] == target:      # Start from edge 1st row, last col
                return True  # Found
            elif matrix[row][col] < target:     # Go DOWN (row++) to search HIGHER values
                row += 1    # eliminate rows
            else:                               # Go LEFT (col--) to search LOWER values
                col -= 1    # eliminate cols

        return False  # Not found

    """ Pattern: Binary Search in 2D Matrix     

    Trick: Convert 2D Index in 1D index ----> for (i, j)  == i * cols + j
        Convert 1D Index in 2D index ----> for i       == (row, col) == (i // cols, i % cols)
        
    Look at explaination of 1D --> 2D and 2D --> 1D index conversion math
    https://leetcode.com/problems/search-a-2d-matrix/discuss/26219/Binary-search-on-an-ordered-matrix
        
    """
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not len(matrix) or not len(matrix[0]):
            return False
        
        rows, cols = len(matrix), len(matrix[0])
        
        low, high = 0, (rows*cols)-1  # Indexes
        
        while low < high:
            mid = (low + high) >> 1 # 1D index
            print(f"low: {low}, high: {high}, mid: {mid}")
            
            # Convert 1D index into 2D matrix index (row, col)
            row, col = mid // cols, mid % cols           
            val = matrix[row][col]
            
            # Binary Search
            if val == target:
                return True
            elif target < val:  
                high = mid - 1          # Move L <-- & Top |
            else:
                low  = mid + 1          # Move R ---> and Down |
                
        
        # Low and High are same here
        row, col = low // cols, low % cols
        if matrix[row][col] == target:
            return True
        else:
            return False        


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
