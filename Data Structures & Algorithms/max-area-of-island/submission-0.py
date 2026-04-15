class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        directions = [[0,1], [0, -1], [1, 0], [-1, 0]]
        max_area = 0

        def dfs(r, c):

            if r >= ROWS or c >= COLS or r < 0 or c < 0 or grid[r][c] == 0:
                return 0

            grid[r][c] = 0
            current_area = 1

            for dr, dc in directions:

                current_area += dfs(dr + r, dc + c)


            return current_area


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    final_area = dfs(r, c)
                    print(final_area)

                    max_area = max(max_area, final_area)

        
        return max_area

                    