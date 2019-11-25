
# 思路: 每次向左或向右或不动，最多走steps步，也就是最多走到steps这一格，而且最多走到length-1
# 所以矩阵最大的长度为1+min(steps,length)+1,这里多生成一个尾部元素0，dp[j-1]使用
# 每一轮，更新从0到min(i,length-1)的数据，因为最多走到i或者length-1，这里用上一轮的状态更新当轮dp的状态

class Solution:
    def numWays(self, steps, length):
        dp=[1]+[0]*(min(length,steps)+1)
        for i in range(1,steps+1):
            copy=dp[:]
            for j in range(min(i+1,length)):
                copy[j]=dp[j-1]+dp[j]+dp[j+1]
            dp=copy
        return dp[0]%(10**9+7)

a=Solution()
print(a.numWays(20,2))
print(a.numWays(3,2))
print(a.numWays(2,4))
print(a.numWays(4,2))