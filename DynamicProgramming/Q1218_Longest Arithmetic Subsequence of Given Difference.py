
# 思路: 每加一个i，寻找i-difference的MaxLength(以i-difference结尾)，更新dp[i]和res

import collections
class Solution:
    def longestSubsequence(self, arr, difference):
        res=0
        dp=collections.defaultdict(int)
        for i in arr:
            dp[i]=max(dp[i],dp[i-difference]+1)
            res=max(res,dp[i])
        return res