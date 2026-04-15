class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROW, COL = len(matrix), len(matrix[0])
        self.preSumMatrix = [[0] * (COL + 1) for r in range(ROW + 1) ]

        for r in range(ROW):
            preSum = 0
            for c in range(COL):
                preSum += matrix[r][c]
                self.preSumMatrix[r+1][c+1] = preSum + self.preSumMatrix[r][c+1]
            

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r1, r2, c1, c2 = row1 + 1, row2 + 1, col1 + 1, col2 + 1

        bottomRight = self.preSumMatrix[r2][c2]
        above = self.preSumMatrix[r1 - 1][c2]
        left = self.preSumMatrix[r2][c1 - 1]
        topleft = self.preSumMatrix[r1 - 1][c1 - 1]

        return bottomRight - above - left + topleft

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)