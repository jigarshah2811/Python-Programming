class Solution:
    def numIslands(self, grid):
        def dfs(row, col):
            # OOB
            if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] == "0":
                return

            # Mark this node visited
            grid[row][col] = "0"

            # DFS Neighbors
            dfs(row-1, col)
            dfs(row, col-1)
            dfs(row+1, col)
            dfs(row, col+1)
            return

        # Start
        if not grid:        # Edge case: grid = []
            return 0

        rows = len(grid)
        cols = len(grid[0])            
        count = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":  # Start visiting nodes only if grid[row][col] = 1
                    print(f"Starting from: ({row}{col})")
                    count += 1
                    dfs(row, col)
    
        return count

s = Solution()
grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
print(s.numIsalnds(grid))     # Output: 1

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
print(s.numIsalnds(grid))     # Output: 3