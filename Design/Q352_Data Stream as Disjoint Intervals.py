# 1, 3, 7, 2, 6, ...,
# [1, 1]
# [1, 1], [3, 3]
# [1, 1], [3, 3], [7, 7]
# [1, 3], [7, 7]
# [1, 3], [6, 7]

# 思路: 用heap存储interval，方便插入(按start排序)，getInterval时，从heap中pop出各个Interval，整合并返回
# 注意要保持self.intervals一直是heap形式存储

import heapq
class SummaryRanges:

    def __init__(self):
        self.intervals=[]

    def addNum(self, val):
        heapq.heappush(self.intervals,[val,val])

    def getIntervals(self):
        merged=[]
        while self.intervals:
            x=heapq.heappop(self.intervals)
            if not merged or x[0]>merged[-1][-1]+1:
                merged.append(x)
            else:
                merged[-1][-1]=max(merged[-1][-1], x[1])
        heapq.heapify(merged)
        self.intervals=merged
        return merged


# Your SummaryRanges object will be instantiated and called as such:
obj = SummaryRanges()
obj.addNum(1)
obj.addNum(3)
print(obj.getIntervals())
obj.addNum(7)
obj.addNum(2)
print(obj.getIntervals())
obj.addNum(6)
print(obj.getIntervals())