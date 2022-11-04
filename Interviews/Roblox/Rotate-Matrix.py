class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Reverse Matrix
        left, right = 0, len(matrix)-1
        while left < right: # SWAP 
            matrix[left], matrix[right] = matrix[right], matrix[left]  
            left += 1       # Move forward --->
            right -= 1      # Move backward <-----
            
        print(f"Reversed Matrix: {matrix}")
        
        
        # Transpose matrix: Ele at (row, col) goes to ele at (col, row)
        rows, cols = len(matrix), len(matrix[0])
        
        for row in range(rows):
            for col in range(row):
                # Swap ele at (row, col) to (col, row)
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
