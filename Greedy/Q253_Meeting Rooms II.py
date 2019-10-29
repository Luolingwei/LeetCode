
# 思路: 按时间的start排序，每来一个interval，判断其start是否小于当前所有room的end时间
# 如果是，必须要新安排一个room，否则将当前interval插入任意一个(这里取堆顶即minend的room)room，更新end即可
# 这里可以插入任意一个的原因是按Start排序之后end如果对当前interval可用对之后的interval将都可用

import heapq
class Solution:
    # O(NlogN)
    def minMeetingRooms(self, intervals):
        intervals.sort(key=lambda x:x[0])
        room_ends=[]
        for start,end in intervals:
            if room_ends and room_ends[0]<=start:
                heapq.heappop(room_ends)
            heapq.heappush(room_ends,end)
        return len(room_ends)

a=Solution()
print(a.minMeetingRooms([[0, 30],[5, 10],[15, 20]]))