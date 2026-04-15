class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        row, col = len(grid), len(grid[0])
        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        nun_of_island = 0

        def dfs(r, c):

            if r >= row or c >= col or grid[r][c] == "0" or r < 0 or c < 0:
                return

            grid[r][c] = "0"

            for dr, dc in direction:
                nr, nc = dr + r, dc + c
                
                dfs(nr, nc)

        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1":
                    
                    dfs(r, c)
                    nun_of_island += 1

        return nun_of_island
