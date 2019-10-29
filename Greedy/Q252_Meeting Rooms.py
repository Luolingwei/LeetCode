
# 按start排序后check每个interval之间是否有重叠

class Solution:
    # Solution 1 O(NlogN)
    # def canAttendMeetings(self, intervals):
    #     intervals.sort(key=lambda x: x[0])
    #     tail=-1
    #     for start,end in intervals:
    #         if start<tail:
    #             return False
    #         else:
    #             tail=end
    #     return True

    # Solution 2 O(NlogN)
    def canAttendMeetings(self, intervals):
        intervals.sort(key=lambda x: x[0])
        for i in range(1,len(intervals)):
            if intervals[i][0]<intervals[i-1][1]:
                return False
        return True