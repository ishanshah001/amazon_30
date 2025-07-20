"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        
        count = 0
        max_count = 0

        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        i = 0
        j=0
        while i< (len(start)):
            if end[j] > start[i]:
                count+=1
                i+=1
            else:
                j+=1
                count-=1
            max_count = max(count, max_count)
                
        return max_count
        