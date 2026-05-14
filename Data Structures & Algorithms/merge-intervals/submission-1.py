class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort()
        while len(intervals) > 0:
            temp = intervals.pop(0)

            if len(res) == 0:
                res.append(temp)

            elif res[-1][1] < temp[0]:
                res.append(temp)

            else:
                temp2 = res.pop()

                res.append([min(temp2[0], temp[0]), max(temp2[1], temp[1])])

        return res