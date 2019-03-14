class Solution:
    def numTrees(self, n):
        dp=[1]*(n+1)
        for i in range(2,n+1):
            temp=0
            for j in range(i):
                temp+=dp[j]*dp[i-j-1]
            dp[i]=temp
        return dp[n]

a=Solution()
print(a.numTrees(3))