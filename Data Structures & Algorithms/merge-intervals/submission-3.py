class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort()
        res = [intervals[0]]
        # while len(intervals) > 0:
        #     temp = intervals.pop(0)

        #     if len(res) == 0:
        #         res.append(temp)

        #     elif res[-1][1] < temp[0]:
        #         res.append(temp)

        #     else:
        #         temp2 = res.pop()

        #         res.append([min(temp2[0], temp[0]), max(temp2[1], temp[1])])

        for i in intervals:
            if res[-1][1] < i[0]:
                res.append(i)

            else:
                res[-1] = [min(i[0], res[-1][0]), max(i[1], res[-1][1])]

        return res