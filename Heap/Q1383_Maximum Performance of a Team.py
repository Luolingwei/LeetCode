
# 思路: 将engineers按efficiency排序，从大到小遍历
# 每一轮表示以当前efficiency为min值，只需要在其前面的engineers中找到k个最大的speed即可
# 用heap维护size为k的speeds

import heapq
class Solution:
    # O(nlogn)
    def maxPerformance(self, n: int, speed, efficiency, k: int):
        speeds = []
        totalSpeed = 0
        res = 0
        for e,s in sorted(zip(efficiency,speed),reverse=True):
            heapq.heappush(speeds,s)
            totalSpeed+=s
            if (len(speeds)>k): totalSpeed-=heapq.heappop(speeds)
            res = max(res,totalSpeed*e)
        return res%(10**9+7)


a=Solution()
print(a.maxPerformance(6,[2,10,3,1,5,8],[5,4,3,9,7,2],2))
print(a.maxPerformance(6,[2,10,3,1,5,8],[5,4,3,9,7,2],3))
print(a.maxPerformance(6,[2,10,3,1,5,8],[5,4,3,9,7,2],4))