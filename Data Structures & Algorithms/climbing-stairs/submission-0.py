class Solution:
    def climbStairs(self, n: int) -> int:
        second_last, last = 1, 1

        for i in range(n-1):
            temp = second_last
            second_last = second_last + last
            last = temp

        return second_last