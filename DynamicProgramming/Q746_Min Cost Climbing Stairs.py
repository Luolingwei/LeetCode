
class Solution:

    # Solution 1 dp[i]代表到达当前梯子所需要的cost, dp[i]=min(dp[i-1]+cost[i-1],dp[i-2]+cost[i-2])
    # def minCostClimbingStairs(self, cost):
    #     dp=[0]*(len(cost)+1)
    #     for i in range(2,len(cost)+1):
    #         dp[i]=min(dp[i-1]+cost[i-1],dp[i-2]+cost[i-2])
    #     return dp[-1]

    # Solution 2 cost[i]代表cover当前梯子所需要的cost, cost[i]=cost[i]+min(cost[i-1],cost[i-2])，返回min(cost[-1],cost[-2])
    def minCostClimbingStairs(self, cost):
        for i in range(2,len(cost)):
            cost[i]+=min(cost[i-1],cost[i-2])
        return min(cost[-1],cost[-2])

a=Solution()
print(a.minCostClimbingStairs([10, 15, 20]))
print(a.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))