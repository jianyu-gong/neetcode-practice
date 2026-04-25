class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        # if obstacleGrid[-1][-1] == 1:
        #     return 0

        ROWS = len(obstacleGrid)
        COLS = len(obstacleGrid[0])

        # previous_row = [0] * COLS
        # obstacleGrid.append(previous_row)

        # for row in range(ROWS - 1, -1, -1):
        #     current_row = [0] * COLS

        #     # current_row[-1] = 1 if obstacleGrid[row][-1] == 0 else 0

        #     for col in range(COLS - 2, -1, -1):

        #         current_row[col] = 0 if obstacleGrid[row][col] == 1 else current_row[col + 1] + previous_row[col]
            
        #     print(f'{current_row=}')
        #     previous_row = current_row
            
        
        # return current_row[0]

        cache = {(ROWS - 1 ,COLS - 1):1}

        def dfs(row, col):

            if row == ROWS or col == COLS or obstacleGrid[row][col] == 1:
                return 0

            if (row, col) in cache:
                return cache[(row, col)]

            cache[(row, col)] = dfs(row + 1, col) + dfs(row, col + 1)

            return cache[(row, col)]

        return dfs(0 , 0)