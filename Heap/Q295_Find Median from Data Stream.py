
# 思路: 维护一个large heap和一个small heap， 每次加入num时保证从large中pop出最小的放到small中
# 为了让large和small的size最大相差1, 当small>large时，把small的元素往large转

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