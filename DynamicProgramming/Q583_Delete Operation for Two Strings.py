# Input: "sea", "eat"
# Output: 2
# Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".

# 思路:dp求最长公共序列

class Solution:
    def minDistance(self, word1, word2):
        m,n=len(word1),len(word2)
        dp=[[0]*(n+1) for _ in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if word1[i-1]==word2[j-1]:
                    dp[i][j]=dp[i-1][j-1]+1
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        return m+n-dp[-1][-1]*2

a=Solution()
print(a.minDistance('sea','eat'))