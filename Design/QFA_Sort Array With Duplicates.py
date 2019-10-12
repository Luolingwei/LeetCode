import heapq
class Solution:

    def __init__(self):
        self.queue=[]
        self.count={}
        self.keys=set()

    def binarySearch(self,target):
        l,r=0,len(self.keys)-1
        while l<r:
            mid=(l+r)//2
            if self.keys[mid]==target:
                return True
            elif self.keys[mid]>target:
                r=mid-1
            else:
                l=mid+1
        return False

    def insert(self,i):
        if i not in self.keys:
            heapq.heappush(self.queue,i)
        self.count[i]=self.count.get(i,0)+1

    def frequency(self,j):
        if j not in self.keys:
            return 0
        return self.count[j]


a=Solution()
a.insert(2)
a.insert(2)
a.insert(2)
a.insert(2)
a.insert(6)
a.insert(6)
print(a.frequency(3))
print(a.frequency(2))