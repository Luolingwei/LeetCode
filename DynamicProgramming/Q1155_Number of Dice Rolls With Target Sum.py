# Input: d = 1, f = 6, target = 3
# Output: 1
# Explanation:
# You throw one die with 6 faces.  There is only one way to get a sum of 3.
#
# Input: d = 2, f = 6, target = 7
# Output: 6
# Explanation:
# You throw two dice, each with 6 faces.  There are 6 ways to get a sum of 7:
# 1+6, 2+5, 3+4, 4+3, 5+2, 6+1.
#
# Input: d = 30, f = 30, target = 500
# Output: 222616187
# Explanation:
# The answer must be returned modulo 10^9 + 7.

# 思路: 最后一个骰子是x，dp[i][target]=sum(dp[i-1][target-x] for x in range(1,f+1) if target-x>0)

class Solution:
    # Solution 1 top-down 668 ms
    # def numRollsToTarget(self, d, f, target):
    #     memo={}
    #     def dp(i,t):
    #         if (i,t) in memo:
    #             return memo[(i,t)]
    #         if t<1: return 0
    #         if i==1:
    #             return 1 if t<=f else 0
    #         memo[(i,t)]=sum(dp(i-1,t-x) for x in range(1,f+1))
    #         return memo[(i,t)]
    #     return dp(d,target)%(10**9+7)

    # Solution 2 bottom-up 904 ms
    def numRollsToTarget(self, d, f, target):
        dp=[[0]*(target+1) for _ in range(d+1)]
        for k in range(1,min(target,f)+1):
            dp[1][k]=1
        for i in range(2,d+1):
            for j in range(1,target+1):
                dp[i][j]=sum(dp[i-1][j-x] for x in range(1,f+1) if j-x>0)
        return dp[d][target]%(10**9+7)

a=Solution()
print(a.numRollsToTarget(1,6,3))
print(a.numRollsToTarget(2,6,7))
print(a.numRollsToTarget(2,5,10))
print(a.numRollsToTarget(30,30,500))
print(a.numRollsToTarget(2,12,8))