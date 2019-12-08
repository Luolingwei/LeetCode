import heapq
import collections
class Solution:
    # k log(m) at most, m is the unique number in array
    def topKFrequent(self, nums, k):
        count=collections.Counter(nums)
        queue=[(-n,c) for c,n in count.items()]
        heapq.heapify(queue)
        return [heapq.heappop(queue)[1] for _ in range(k)]

a=Solution()
print(a.topKFrequent([1,1,1,2,2,3],2))
print(a.topKFrequent([1,1,1],1))
print(a.topKFrequent([1],1))