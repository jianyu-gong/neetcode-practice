class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        # grid = [[0] * n for i in range(m)]
        # print(grid)
        previous_row = [0] * n

        for row in range(m - 1, -1, -1):

            current_row = [0] * n
            current_row[-1] = 1

            for col in range(n - 2, -1, -1):

                current_row[col] = current_row[col + 1] + previous_row[col]
            previous_row = current_row
                


        return current_row[0]