class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        up = 0
        down = len(matrix) - 1

        while up <= down:
            mid = (up + down) // 2

            if target < matrix[mid][0]:
                down = mid - 1
            elif target > matrix[mid][0]:
                up = mid + 1
            else:
                return True

        row = mid - 1 if target < matrix[mid][0] else mid
        print(row)

        left = 0
        right = len(matrix[0]) - 1

        while left <= right:
            mid = (left + right) // 2

            if target < matrix[row][mid]:
                right = mid - 1

            elif target > matrix[row][mid]:
                left = mid + 1

            else:
                return True

        return False