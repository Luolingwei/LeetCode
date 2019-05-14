# "bbbab"
# 4
# "cbbd"
# 2

# 思路: dp，对于每一个长度范围(1-len(s))的最长回文length,如果s[i]==s[j]（i,j为两头的坐标）,dp[i][j]=dp[i+1][j-1]+2，否则dp[i][j]=max(dp[i+1][j],dp[i][j-1]),gap从0到len(s)-1变化

class Solution:
    def longestPalindromeSubseq(self, s):
        if not s: return 0
        l=len(s)
        dp=[[0]*l for _ in range(l)]
        for gap in range(l):
            for left in range(l-gap):
                right=left+gap
                if left==right:
                    dp[left][right]=1
                else:
                    if s[left]==s[right]:
                        dp[left][right]=dp[left+1][right-1]+2
                    else:
                        dp[left][right]=max(dp[left+1][right],dp[left][right-1])
        return dp[0][l-1]

a=Solution()
print(a.longestPalindromeSubseq("bbbab"))
print(a.longestPalindromeSubseq("cbbd"))
print(a.longestPalindromeSubseq(""))