
# 思路: 考虑s[i]和s[j]是否相等, dp[i][j]=dp[i+1][j-1] if s[i]==s[j] else min(dp[i+1][j],dp[i][j-1])+1

class Solution:
    def minInsertions(self, s):
        N=len(s)
        dp=[[0]*(N+1) for _ in range(N+1)]
        for gap in range(N):
            for left in range(N-gap):
                right=left+gap
                if s[left]==s[right]:
                    dp[left][right]=dp[left+1][right-1]
                else:
                    dp[left][right]=min(dp[left+1][right],dp[left][right-1])+1
        return dp[0][N-1]

a=Solution()
print(a.minInsertions("zzazz"))
print(a.minInsertions("mbadm"))
print(a.minInsertions("leetcode"))
print(a.minInsertions("g"))
print(a.minInsertions("no"))