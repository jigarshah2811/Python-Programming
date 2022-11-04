""" Valid Sudoku
https://leetcode.com/problems/valid-sudoku/submissions/
"""
import collections
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols = len(board), len(board[0])

        """
        DS:         Tuple Map
        Pattern:    To spot dup in rows:  {Key: (Row#, #)  --->  Value: True/False }
                    To spot dup in cols:  {Key: (Col#, #)  --->  Value: True/False }
                    To spot dup in boxes: {Key: (Box#, #)  --->  Value: True/False }
        """        
        seenRow = collections.defaultdict(bool)
        seenCol = collections.defaultdict(bool)
        seenBox = collections.defaultdict(bool)
        
        for row in range(rows):
            for col in range(cols):
                val = board[row][col]
                if val != ".":
                    
                    # Check if it already exists in the same row
                    if seenRow[(row, val)]: # exists
                        return False
                    elif seenCol[(col, val)]:  # exists
                        return False
                    elif seenBox[(row//3, col//3, val)]:
                        return False
                    else:
                        # Mark "num" in corresponding ROW COL and BOX, to spot if it's seen next time!           
                        seenRow[(row, val)] = True
                        seenCol[(col, val)] = True
                        seenBox[(row//3, col//3, val)] = True
        
        
        # Entire sudoku completed validation, no 'False' for rows, cols or boxes
        return True