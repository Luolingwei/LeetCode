# Input: A = [1,15,7,9,2,5,10], K = 3
# Output: 84
# Explanation: A becomes [15,15,15,9,10,10,10]

# 思路: dp，最后一次添加的子数组长度为1到k，所以每次回溯1到k个长度，并记录回溯过程中的最大值，作为最后加进来数组的值。

class Solution:
    def maxSumAfterPartitioning(self, A, K):
        dp=[0]*(len(A)+1)
        for i in range(1,len(A)+1):
            curmax=0
            for j in range(1,min(i,K)+1):
                curmax=max(curmax,A[i-j])
                dp[i]=max(dp[i],dp[i-j]+curmax*j)
        return dp[-1]

a=Solution()
print(a.maxSumAfterPartitioning([1,15,7,9,2,5,10],3))
print(a.maxSumAfterPartitioning([3,7],2))




