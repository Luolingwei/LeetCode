import heapq
import collections
class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        C,queue=collections.Counter(nums),[]
        for n in C:
            heapq.heappush(queue,(-C[n],n))
        return [heapq.heappop(queue)[1] for _ in range(k)]

a=Solution()
print(a.topKFrequent([1,1,1,2,2,3],2))
print(a.topKFrequent([1,1,1],1))
print(a.topKFrequent([1],1))