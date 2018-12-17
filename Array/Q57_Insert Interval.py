# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals):
        intervals.sort(key=lambda x: x.start)
        merged = []
        for x in intervals:
            if merged == [] or merged[-1].end < x.start:
                merged.append(x)
            else:
                merged[-1].end = max(merged[-1].end, x.end)
        return merged

    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        if len(intervals) == 0:
            return [newInterval]
        i = 0
        while i < (len(intervals)):
            if intervals[i].start > newInterval.start:
                break
            i += 1
        intervals.insert(i, newInterval)
        return self.merge(intervals)