# Input: quality = [10,20,5], wage = [70,50,30], K = 2
# Output: 105.00000
# Explanation: We pay 70 to 0-th worker and 35 to 2-th worker.

# 思路: ratio=wage/quality, 要保证所有人的工资和quality成比例，那么ratio相同，如果以某个worker的ratio为标准，那么需要在比其ratio小的worker中选k-1个quality最小的.
# 所以先按ratio从小到大排序，并用heap保存k-1个最小的quality. 从第一个到最后一个选择ratio并更新ans

import heapq
class Solution:
    def mincostToHireWorkers(self, quality, wage, K):
        workers=sorted([(w/q,q) for (w,q) in zip(wage,quality)])
        ans,queue,qSum=float('inf'),[],0
        for i in range(len(workers)):
            ratio,q=workers[i]
            qSum+=q
            heapq.heappush(queue,-q)
            if len(queue)>K:
                qSum+=heapq.heappop(queue)
            if i>=K-1:
                ans=min(ans,qSum*ratio)
        return ans


a=Solution()
print(a.mincostToHireWorkers([3,1,10,10,1],[4,8,2,2,7],3))
print(a.mincostToHireWorkers([10,20,5],[70,50,30],2))