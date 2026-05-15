"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # create a start time and end time List
        start_time = [i.start for i in intervals]
        end_time = [i.end for i in intervals]
        
        # sort two lists
        start_time.sort()
        end_time.sort()

        # initialize two pointer
        s, e = 0, 0

        res = 0
        room_needed = 0

        while s < len(intervals) and e < len(intervals):
            if start_time[s] < end_time[e]:
                room_needed += 1
                s += 1

            else:
                room_needed -= 1
                e += 1

            res = max(res, room_needed)

        return res