
# 思路: 考虑最后两个连接的人，他们将circle分割成左右两部分，一共剩下i-2个人，因为左右两边必须时偶数个人，所有l增加的步长为2
# 将所有可能的l和r的组合加起来就是dp[i]

class Solution:
    def numberOfWays(self, n):
        dp=[1]+[0]*n
        for i in range(2,n+1,2):
            j=i-2
            for l in range(0,j+1,2):
                r=j-l
                dp[i]+=dp[l]*dp[r]
        return dp[-1]%(10**9+7)

a=Solution()
print(a.numberOfWays(2))
print(a.numberOfWays(4))
print(a.numberOfWays(6))
print(a.numberOfWays(8))