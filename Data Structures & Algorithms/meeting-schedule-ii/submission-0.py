"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # If no class, return 0

        if len(intervals) == 0:
            return 0


        intervals.sort(key=lambda i: i.start)

        end_time = intervals[0].end
        res = 1

        for i in range(1, len(intervals)):

            if intervals[i].start < end_time:
                res += 1

                # find min value of current end time and current interval end time
                end_time = min(end_time, intervals[i].end)

            else:
                end_time = intervals[i].end

        
        return res