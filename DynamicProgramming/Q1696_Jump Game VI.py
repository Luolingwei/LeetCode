
# 思路: dp[i]表示到达第i个位置可以获得的最大sum, dp[i] = max(dp[i-1]...dp[i-k]) + nums[i], 求前k个最大值可以用单调栈
# O(n)

from collections import deque
class Solution:
    def maxResult(self, nums, k):
        N = len(nums)
        dp = [nums[0]]+ [0]*(N-1)
        q = deque([0])
        for i in range(1,N):
            dp[i]= dp[q[0]] + nums[i]
            while q and dp[q[-1]]<dp[i]:
                q.pop()
            q.append(i)
            if q[0] == i-k:
                q.popleft()
        return dp[-1]


a=Solution()
print(a.maxResult([1,-1,-2,4,-7,3],2))
print(a.maxResult([10,-5,-2,4,0,3],3))
print(a.maxResult([1,-5,-20,4,-1,3,-6,-3],2))