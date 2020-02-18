
# 思路: 将event排序，end小的放前面，end相同的start小的放前面
# 拿到一个event, 如果start不在当前days里，直接在start执行
# 否则从start+1开始搜索可以执行的最小日期

class Solution:
    def maxEvents(self, events):
        events.sort(key=lambda x: (x[1], x[0]))
        days = set()
        for start, end in events:
            if start not in days:
                days.add(start)
            else:
                i = start + 1
                while i in days:
                    i += 1
                if i <= end:
                    days.add(i)
        return len(days)

a=Solution()
print(a.maxEvents([[1,10],[2,2],[2,2],[2,2],[2,2]]))
print(a.maxEvents([[1,5],[1,5],[1,5],[2,3],[2,3]]))
print(a.maxEvents([[1,2],[1,2],[3,3],[1,5],[1,5]]))