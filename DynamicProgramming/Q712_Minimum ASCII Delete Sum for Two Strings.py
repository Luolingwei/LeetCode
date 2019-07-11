# Input: s1 = "sea", s2 = "eat"
# Output: 231
# Explanation: Deleting "s" from "sea" adds the ASCII value of "s" (115) to the sum.
# Deleting "t" from "eat" adds 116 to the sum.
# At the end, both strings are equal, and 115 + 116 = 231 is the minimum sum possible to achieve this.

# 思路: 寻找公共子序列的最大ord值，然后用总ord值减2*dp[-1][-1]即可得到删除的ASCII值.

class Solution:
    def minimumDeleteSum(self, s1, s2):
        m,n=len(s1),len(s2)
        dp=[[0]*(n+1) for _ in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if s1[i-1]==s2[j-1]:
                    dp[i][j]=dp[i-1][j-1]+ord(s1[i-1])
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        return sum(map(ord,s1+s2))-dp[-1][-1]*2

a=Solution()
print(a.minimumDeleteSum("sea","eat"))
print(a.minimumDeleteSum("delete","leet"))
print(a.minimumDeleteSum("ccaccjp","fwosarcwge"))