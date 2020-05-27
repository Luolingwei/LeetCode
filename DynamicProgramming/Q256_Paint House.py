
# dp, 用三个数字分别记录paint完上一个房子用red,blue,green所需要的最小cost
# 那么 dp[0] = min(dp[1]+dp[2]+a), 以此类推
# 最后返回min(dp)

class Solution:
    def minCost(self, costs):
        dp = [0,0,0]
        for a,b,c in costs:
            dp[0],dp[1],dp[2] = min(dp[1],dp[2])+a,min(dp[0],dp[2])+b,min(dp[0],dp[1])+c
        return min(dp)

a=Solution()
print(a.minCost([[17,2,17],[16,16,5],[14,3,19]]))