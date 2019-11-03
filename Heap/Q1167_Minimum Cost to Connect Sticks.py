
# 思路: 每次拿最小的两个进行merge，因为最先被merge会被用最多次

import heapq
class Solution:
    # O(nlogn)
    def connectSticks(self, sticks):
        heapq.heapify(sticks)
        ans=0
        while len(sticks)>1:
            a=heapq.heappop(sticks)
            b=heapq.heappop(sticks)
            ans+=(a+b)
            heapq.heappush(sticks,a+b)
        return ans

a=Solution()
print(a.connectSticks([2,4,3]))
print(a.connectSticks([1,8,3,5]))