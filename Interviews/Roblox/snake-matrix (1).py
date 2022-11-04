import collections
class Solution:
    """ Checks valid paths from grid
        returns rows=[] and cols=[] 
    """
    def checkValidRowsCols(self, grid):
        rows, cols = len(grid), len(grid[0])

        # Go row by row and find out valid rows
        validRows = []
        for row in range(rows):
            validRow = True
            for col in range(cols):
                if grid[row][col] != "0":   # not a valid path snake can move
                    validRow = False
                    break
            if validRow:
                validRows.append(row)
        
        # Scan col by col and find out valid cols
        validCols = []
        for col in range(cols):
            validCol = True     # by-default this col is valid, until we find a non "0"
            for row in range(rows):
                if grid[row][col] != "0":   # not a valid path snake can move
                    validCol = False
                    break
            
            if validCol:
                validCols.append(col)
        
        return validRows, validCols
    # Find if there is a path from SRC to DEST in same row for snake, return hops
    def findPath_dfs(self, grid, srcRow, srcCol):
        rows, cols = len(grid), len(grid[0])
        self.hops = 0

        def dfs(row, col):
            # Only explore valid path
            if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] != "0":
                return 0

            # Check if we reached dest!
            if row == srcRow and col != srcCol:
                print(f"Bingo! Found path ending at: ({row},{col})")
                return self.hops + 1

            grid[row][col] = "1"
            self.hops += 1
            print(f"Visited ({row},{col})")
            # Explore all neighbors
            return dfs(row+1, col) or \
                    dfs(row, col+1) or \
                    dfs(row-1, col) or \
                    dfs(row, col-1) 

            # If no path exists
            return 0
            
        pathExists = dfs(srcRow, srcCol)
        return pathExists
    
    def findPath_bfs(self, grid, srcRow, srcCol):
        rows, cols = len(grid), len(grid[0])
        q = collections.deque([(srcRow, srcCol)])
        hops = -1
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        while q:            
            totalCells = len(q)
            hops += 1
            print(f"Level: {hops}, Q: {q}")

            while totalCells > 0:
                row, col = q.popleft()
                # Check for target
                if row == srcRow and col != srcCol:
                    print(f"Bingo! We reached target at: ({row},{col})")
                    return hops
                
                # Mark this node visited
                grid[row][col] = "1"
                print(f"visited: ({row},{col})")

                # EXplore all neighbors from here
                for (diffRow, diffCol) in directions:
                    nextRow, nextCol = row + diffRow, col + diffCol
                    if nextRow < 0 or nextRow >= rows or nextCol < 0 or nextCol >= cols or grid[nextRow][nextCol] != "0":
                        continue
                    q.append((nextRow, nextCol))

                totalCells -= 1
    

s = Solution()
grid = [
['+', '+', '+', '0', '+', '0', '0'],
['0', '0', '0', '0', '0', '0', '0'],
['0', '0', '+', '0', '0', '0', '0'],
['0', '0', '0', '0', '+', '0', '0'],
['+', '+', '+', '0', '0', '0', '+']]

print(s.checkValidRowsCols(grid))           # Expected (validRows: [1], validCols: [3, 5])

# A path from SRC to DEST in same row for snake
srcRow, srcCol = 0, 3
# print(s.findPath_dfs(grid, srcRow, srcCol))
print(s.findPath_bfs(grid, srcRow, srcCol))