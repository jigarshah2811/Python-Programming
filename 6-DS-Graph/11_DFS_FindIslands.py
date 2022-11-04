import collections

class SolutionDFS:
    def numIslands(self, grid):
        if not grid:
            return 0

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':       # Explore an island from this land, mark all surronding land "1" = part of this island
                    self.dfs(grid, i, j)
                    count += 1
        return count

    def dfs(self, grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1':
            return
        grid[i][j] = '#'        # Mark this land VISITED to prevent visiting again through DFS
        self.dfs(grid, i + 1, j)
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i, j + 1)
        self.dfs(grid, i, j - 1)


class SolutionBFS:
    q = collections.deque()

    def numIsalnds(self, grid):
        if not grid:
            return 0

        def BFS():
            while q:
                (i, j) = q.popleft()
                if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1':
                    return
                grid[i][j] = '#'

                q.append((i + 1, j))
                q.append((i - 1, j))
                q.append((i, j + 1))
                q.append((i + 1, j-1))

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    q.append(grid[i][j])
                    BFS()
                    q = []
                    count += 1
