# Input: "aaabbb"
# Output: 2
# Explanation: Print "aaa" first and then print "bbb".
#
# Input: "aba"
# Output: 2
# Explanation: Print "aaa" first and then print "b" from the second place of the string, which will cover the existing character 'a'.

# 思路: 考虑dp[left][right]，dp[left]可以和后面的一起打印，如果s[left]==s[k]，dp[left][right]=min(dp[left+1][k]+dp[k+1][right]),(k个后面的在同一个turn打印出来,left+1<=k<=right)
# 注意可能后面没有和dp[left]相同的字母，所以将dp[left][right]初始化为1+dp[left+1][right](单独打印dp[left])

class Solution:
    def strangePrinter(self, s):
        N=len(s)
        dp=[[0]*(N+1) for _ in range(N+2)]
        for i in range(1,N+1):
            dp[i][i]=1
        for gap in range(1,N):
            for left in range(1,N+1-gap):
                right=left+gap
                dp[left][right]=1+dp[left+1][right]
                for k in range(left+1,right+1):
                    if s[k-1]==s[left-1]:
                        dp[left][right]=min(dp[left][right],dp[left+1][k]+dp[k+1][right])
        return dp[1][N]

a=Solution()
print(a.strangePrinter("aaabbb"))
print(a.strangePrinter("aba"))
print(a.strangePrinter("abbbbbcax"))