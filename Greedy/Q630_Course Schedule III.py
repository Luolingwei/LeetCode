# Input: [[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]
# Output: 3
# Explanation:
# There're totally 4 courses, but you can take 3 courses at most:
# First, take the 1st course, it costs 100 days so you will finish it on the 100th day, and ready to take the next course on the 101st day.
# Second, take the 3rd course, it costs 1000 days so you will finish it on the 1100th day, and ready to take the next course on the 1101st day.
# Third, take the 2nd course, it costs 200 days so you will finish it on the 1300th day.
# The 4th course cannot be taken now, since you will finish it on the 3300th day, which exceeds the closed date.

# 思路: 将课程按结束时间排序，考虑前k个课程，需要在第k个end之前修尽量多的课程.
# 每修一个课程，如果当前的结束时间大于end，那么丢弃掉前面用时最长的课程，修改curD，使得其尽可能小(修的课程数量一样，如果超时，来一个丢一个)

import heapq
class Solution:
    def scheduleCourse(self, courses):
        queue,curD=[],0
        for time,ddl in sorted(courses,key=lambda x:x[1]):
            curD+=time
            heapq.heappush(queue,-time)
            if curD>ddl:
                curD+=heapq.heappop(queue)
        return len(queue)

a=Solution()
print(a.scheduleCourse([[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]))
print(a.scheduleCourse([[5,5],[4,6],[2,6]]))