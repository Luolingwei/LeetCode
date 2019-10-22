
# 思路1: 以start排序，每来一个start,end,profit, 与之前的比较，计算当前end能取得的最大profit
# 思路2: 以end排序，每来一个start,end,profit，与之前的比较，binary search 计算当前end能取得的最大profit
# 如果当前能取得的profit大于前面的，append到queue里，否则当前job不做，queue不更新

import bisect
import collections
class Solution:
    # Solution 1 TLE O(n^2)
    # def jobScheduling(self, startTime, endTime, profit):
    #     N=len(startTime)
    #     jobs=sorted([(startTime[i],endTime[i],profit[i]) for i in range(N)])
    #     dp=collections.defaultdict(int)
    #     dp[0]=0
    #     for start,end,p in jobs:
    #         for preend in list(dp.keys()):
    #             if preend<=start:
    #                 dp[end]=max(dp[end],dp[preend]+p)
    #     return max(dp.values())

    # Solution 2 由于这里profit是升序，只需要用bisect查找之前的maxprofit，O(nlogn)
    def jobScheduling(self, startTime, endTime, profit):
        jobs=sorted(zip(startTime,endTime,profit),key=lambda x:x[1])
        queue=[[0,0]]
        for start,end,p in jobs:
            idx=bisect.bisect_left(queue,[start,float('inf')])-1
            if queue[idx][1]+p>queue[-1][1]:
                queue.append([end,queue[idx][1]+p])
        return queue[-1][1]


a=Solution()
print(a.jobScheduling([1,2,3,3],[3,4,5,6],[50,10,40,70]))
print(a.jobScheduling([1,2,3,4,6],[3,5,10,6,9],[20,20,100,70,60]))
print(a.jobScheduling([1,1,1],[2,3,4],[5,6,4]))
print(a.jobScheduling([6,15,7,11,1,3,16,2],[19,18,19,16,10,8,19,8],[2,9,1,19,5,7,3,19]))