class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def over_hour(k):
            total_hours = 0

            for p in piles:
                if p % k == 0:
                    total_hours += p // k

                else:
                    total_hours = total_hours + (p // k) + 1

            return total_hours > h

        left = 1
        right = max(piles)

        while left < right:
            mid = (left + right) // 2

            if over_hour(mid):
                left = mid + 1

            else:
                right = mid

        return left if not over_hour(left) else right
