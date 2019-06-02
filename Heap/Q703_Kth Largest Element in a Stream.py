from heapq import *
class KthLargest:

    def __init__(self, k: int, nums):
        heapify(nums)
        self.large,self.small=nums,[]
        self.k=k

    def add(self, val: int):
        heappush(self.small,-heappushpop(self.large,val))
        while len(self.large)>self.k-1:
            heappush(self.small,-heappop(self.large))
        return -self.small[0]



# Your KthLargest object will be instantiated and called as such:
obj = KthLargest(3, [4,5,8,2])
print(obj.add(3))
print(obj.add(5))
print(obj.add(10))
print(obj.add(9))
print(obj.add(4))