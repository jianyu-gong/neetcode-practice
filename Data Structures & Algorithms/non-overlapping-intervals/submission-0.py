class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = 0

        intervals.sort()

        min_l, min_r = intervals.pop(0)

        while intervals:
            l, r = intervals.pop(0)

            if l < min_r:
                res += 1

                min_r = min(r, min_r)

            else:
                min_r = r
                



        return res