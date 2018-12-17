# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    """
    :type intervals: List[Interval]
    :rtype: List[Interval]
    """
    def merge(self, intervals):
        intervals.sort(key=lambda x: x.start)
        merged = []
        for x in intervals:
            if merged == [] or merged[-1].end < x.start:
                merged.append(x)
            else:
                merged[-1].end = max(merged[-1].end, x.end)
        return merged