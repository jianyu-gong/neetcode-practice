class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.preSumMatrix = []
        for m in matrix:
            preSumRow = []
            total  = 0
            for c in m:
                total += c
                preSumRow.append(total)
            self.preSumMatrix.append(preSumRow)
                

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:

        res = 0
        left = col1 - 1 if col1 > 0 else 0
        right = col2
        for i in range(row1, row2+1):
            res += (self.preSumMatrix[i][right] - self.preSumMatrix[i][left])

        return res

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)