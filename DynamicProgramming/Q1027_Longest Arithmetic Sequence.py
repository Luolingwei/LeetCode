# Input: [9,4,7,2,10]
# Output: 3
# Explanation:
# The longest arithmetic subsequence is [4,7,10].

# 思路: dp,用dp[i,v]记录以i结尾的gap为v的最大长度,每次新加一个元素，更新dp的dic

import collections
class Solution:
    def longestArithSeqLength(self, A):
        res=0
        dp=collections.defaultdict(int)
        for i in range(len(A)):
            for j in range(i):
                v=A[i]-A[j]
                dp[i,v]=max(dp[i,v],dp[j,v]+1)
                res=max(res,dp[i,v])
        return res+1

a=Solution()
print(a.longestArithSeqLength([1,2,3]))