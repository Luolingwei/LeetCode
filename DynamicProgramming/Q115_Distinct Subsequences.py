# Input: S = "rabbbit", T = "rabbit"
# Output: 3

# 思路: 考虑 i,j结尾的S和T, 分两种情况，S[i]用上了或者没用上(S[i]==T[i])
# 1 相等: dp[i][j]=dp[i-1][j]+dp[i-1][j-1]
# 2 不相等: dp[i][j]=dp[i-1][j]
# 注意初始化让dp[i][0]=1，意思是T为空时，S不管多长都有一种方法变成T

class Solution:
    def numDistinct(self, s, t):
        m,n=len(s),len(t)
        dp=[[0]*(n+1) for _ in range(m+1)]
        for i in range(m+1):
            dp[i][0]=1
        for i in range(1,m+1):
            for j in range(1,n+1):
                dp[i][j]=dp[i-1][j]+dp[i-1][j-1]*(s[i-1]==t[j-1])
        return dp[-1][-1]

a=Solution()
print(a.numDistinct("babgbag","bag"))
print(a.numDistinct("rabbbit","rabbit"))