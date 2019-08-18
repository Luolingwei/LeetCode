# Input: text1 = "abcde", text2 = "ace"
# Output: 3
# Explanation: The longest common subsequence is "ace" and its length is 3.

# 思路: 求最长公共子序列

class Solution:
    def longestCommonSubsequence(self, text1, text2):
        l1,l2=len(text1),len(text2)
        dp=[[0]*(l2+1) for _ in range(l1+1)]
        for i in range(1,l1+1):
            for j in range(1,l2+1):
                if text1[i-1]==text2[j-1]:
                    dp[i][j]=dp[i-1][j-1]+1
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        return dp[-1][-1]

a=Solution()
print(a.longestCommonSubsequence("abcde","ace"))
print(a.longestCommonSubsequence("abc","abc"))
print(a.longestCommonSubsequence("abc","def"))