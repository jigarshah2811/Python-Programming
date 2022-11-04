""" DS: Graph   Representation: MATRIX      Algorithm: DFS 

Start from path where 1st char matches, Recursively Explore the path to see all remaining char matches 

"""
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if word == "":
            return True
        if board == []:
            return False
    
        
        rows, cols = len(board), len(board[0])
        
        def dfs(row, col, word):
            if len(word) == 0:  # Everything matched
                return True
            
            # OOB? No-match? 
            if row < 0 or row >= rows or col < 0 or col >= cols or board[row][col] != word[0]:
                return False
            
            # print(f"visiting ({row},{col}): {board[row][col]}")
            # Prevent visiting same path again            
            board[row][col] = "#"            


            res = dfs(row+1, col, word[1:]) or \
                  dfs(row-1, col, word[1:]) or \
                  dfs(row, col+1, word[1:]) or \
                  dfs(row, col-1, word[1:])

            # Restore original value
            board[row][col] = word[0]
            return res
                
                
        for row in range(rows):
            for col in range(cols):
                if dfs(row, col, word):     # Explore potential path from here
                    return True             # Full match!
    
        return False
