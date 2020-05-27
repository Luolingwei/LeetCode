import heapq

# 思路: 用一个heap存储用各种颜色paint完上一个house所用的mincost
# paint新house时, 需要从heap选择最小的precost, 只要当前paint的颜色跟之前不同
# 不同时, 选择heap中pop出来的最小cost
# 如果当前使用的颜色和之前的最小值相同, 那么选择第二小的即可
# O(nk)

class Solution:
    def minCostII(self, costs):
        if not costs: return 0
        if len(costs[0])==1: return costs[0][0]
        n,k = len(costs), len(costs[0])
        dp =[(0,i) for i in range(k)]
        heapq.heapify(dp)
        for i in range(n):
            c = costs[i]
            premin, idx = heapq.heappop(dp)
            new_dp = []
            for j in range(k):
                if j!=idx:
                    new_dp.append((c[j]+premin,j))
                else:
                    new_dp.append((c[j]+dp[0][0],j))
            dp = new_dp
            heapq.heapify(dp)
        return heapq.heappop(dp)[0]


a=Solution()
print(a.minCostII([[1,5,3],[2,9,4]]))
print(a.minCostII([]))
print(a.minCostII([[8]]))