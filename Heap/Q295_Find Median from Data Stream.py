
# 思路: 用两个heap分别存储数据流大的一半(large)和小的一半(small)，其中小的一半的heap以负数存储，这样就可以在求median的时候直接取large和small的最小数字了。
# 为了保证large和small的size差距不超过1，每次新进一个数字的时候先用heappushpop操作large，然后pop出的最小数导入small，如果small的size超过了large，将samll的最小数（负的最多）放回large中.

from heapq import *
class MedianFinder:

    # addNum(1)
    # addNum(2)
    # findMedian() -> 1.5
    # addNum(3)
    # findMedian() -> 2

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.large,self.small=[],[]

    def addNum(self, num: int) -> None:
        heappush(self.small,-heappushpop(self.large,num))
        if len(self.small)>len(self.large):
            heappush(self.large,-heappop(self.small))

    def findMedian(self) -> float:
        if len(self.large)>len(self.small):
            return float(self.large[0])
        else:
            return (self.large[0]-self.small[0])/2.0


# Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()
obj.addNum(6)
print(obj.findMedian())
obj.addNum(10)
print(obj.findMedian())
obj.addNum(2)
print(obj.findMedian())
obj.addNum(6)
print(obj.findMedian())
obj.addNum(5)
print(obj.findMedian())
obj.addNum(0)
print(obj.findMedian())
obj.addNum(6)
print(obj.findMedian())
obj.addNum(3)
print(obj.findMedian())
obj.addNum(1)
print(obj.findMedian())
obj.addNum(0)
print(obj.findMedian())
obj.addNum(0)
print(obj.findMedian())