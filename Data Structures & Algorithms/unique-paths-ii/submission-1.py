class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])

        dp = [0] * COLS
        dp[-1] = 1

        for row in range(ROWS - 1, -1, -1):
            for col in range(COLS - 1, -1, -1):
                if obstacleGrid[row][col] == 1:

                    dp[col] = 0
                elif col + 1 < COLS:
                    dp[col] += dp[col + 1]
            
            # print(f'{current_row=}')
            # previous_row = current_row
            
        
        return dp[0]

        # cache = {(ROWS - 1 ,COLS - 1):1}

        # def dfs(row, col):

        #     if row == ROWS or col == COLS or obstacleGrid[row][col] == 1:
        #         return 0

        #     if (row, col) in cache:
        #         return cache[(row, col)]

        #     cache[(row, col)] = dfs(row + 1, col) + dfs(row, col + 1)

        #     return cache[(row, col)]

        # return dfs(0 , 0)