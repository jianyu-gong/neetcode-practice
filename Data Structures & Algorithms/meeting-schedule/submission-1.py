"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) == 0:
            return True

        intervals.sort(key= lambda i: i.start)

        end_time = intervals[0].end

        for i in range(1, len(intervals)):
            if intervals[i].start < end_time:
                return False
            else:
                end_time = intervals[i].end

        return True