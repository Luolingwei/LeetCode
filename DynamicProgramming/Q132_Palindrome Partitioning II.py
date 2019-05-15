# Input: "aab"
# Output: 1
# Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.

# 思路: dp[i]（s[:i]所需的mincut）等于min(dp[j]+1 if s[j:i]是回文)，其中j从0到i移动.dp[0]=-1

class Solution:
    def minCut(self, s):
        l,t=len(s),s[::-1]
        def helper(i,j):
            return s[i:j]==t[l-j:l-i]
        dp=[-1]+[0]*l
        for i in range(1,l+1):
            dp[i]=min(dp[j]+1 for j in range(i) if helper(j,i))
        return dp[-1] if dp[-1]!=-1 else 0

a=Solution()
print(a.minCut('aba'))
print(a.minCut('aab'))
print(a.minCut('ab'))
print(a.minCut(''))