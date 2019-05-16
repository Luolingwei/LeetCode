# Input: word1 = "intention", word2 = "execution"
# Output: 5
# Explanation:
# intention -> inention (remove 't')
# inention -> enention (replace 'i' with 'e')
# enention -> exention (replace 'n' with 'x')
# exention -> exection (replace 'n' with 'c')
# exection -> execution (insert 'u')

# 思路: 以word1和word2为dp的对象，dp[i][j]=min(dp[i-1][j]+1:多一个delete word1[i-1]的操作，dp[i][j-1]+1:多一个insert word2[j-1]的操作，dp[i-1][j-1]+1 if word1[i-1]!=word2[j-1] else +0，多一个replace word1[i-1]和word2[j-1]的操作)
# dp[0][j]=j,dp[i][0]=i

class Solution:
    def minDistance(self, word1, word2):
        l1,l2=len(word1)+1,len(word2)+1
        dp=[[0]*l2 for _ in range(l1)]
        for i in range(l1): dp[i][0]=i
        for j in range(l2): dp[0][j]=j
        for i in range(1,l1):
            for j in range(1,l2):
                dp[i][j]=min(dp[i-1][j]+1,dp[i][j-1]+1,dp[i-1][j-1]+(word1[i-1]!=word2[j-1]))
        return dp[-1][-1]

a=Solution()
print(a.minDistance("intention","execution"))