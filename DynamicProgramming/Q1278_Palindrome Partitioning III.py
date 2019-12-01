
# 思路:  长度m的string分成k个回文，考虑dp,前i长度分成k-1个+最后一个所需的转换数，用prematrix(count)提前存i到j的转换数

class Solution:
    def palindromePartition(self, s, k):
        m = len(s)
        count = [[0] * m for _ in range(m)]
        for i in range(m):
            for j in range(i + 1, m):
                count[i][j] = self.helper(i, j, s)

        dp = [[float('inf')] * (k + 1) for _ in range(m + 1)]
        dp[0][0]=0
        for i in range(1, m + 1):
            for j in range(1, k + 1):
                for pre in range(i):
                    dp[i][j] = min(dp[i][j],dp[pre][j - 1] + count[pre][i - 1])
        return dp[-1][-1]

    def helper(self, i, j, s):
        res = 0
        while i < j:
            if s[i] != s[j]:
                res += 1
            i += 1
            j -= 1
        return res

a=Solution()
print(a.palindromePartition("abc",2))
print(a.palindromePartition("aabbc",3))
print(a.palindromePartition("leetcode",8))