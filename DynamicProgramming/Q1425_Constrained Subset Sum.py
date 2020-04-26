from collections import deque

# 思路1: dp, 考虑最后一个选择数字, dp[i] = max(dp[i-k]...dp[i-1]) + nums[i] O(N*k)
# 思路2: 用单调deque优化，使得取前面k个的最大值变为O(1), 即sliding window maximum

class Solution:

    # O(Nk)
    def constrainedSubsetSum(self, nums, k: int) -> int:
        N = len(nums)
        ans = nums[0]
        dp = [nums[0]] + [0]*(N-1)
        for i in range(1,N):
            curmax = max(dp[j] for j in range(i-k,i))
            dp[i]= max(nums[i],curmax + nums[i])
            ans = max(dp[i], ans)
        return ans

    # O(N)
    def constrainedSubsetSum(self, nums, k: int) -> int:
        N = len(nums)
        ans = nums[0]
        dp = [nums[0]] + [0]*(N-1)
        q = deque([0])
        for i in range(1,N):
            curmax = dp[q[0]]
            dp[i]= max(nums[i],curmax + nums[i])
            ans = max(dp[i], ans)
            while q and dp[q[-1]]<dp[i]:
                q.pop()
            q.append(i)
            if q[0] == i-k:
                q.popleft()
        return ans


a=Solution()
print(a.constrainedSubsetSum([10,2,-10,5,20],2))
print(a.constrainedSubsetSum([-1,-2,-3],1))
print(a.constrainedSubsetSum([10,-2,-10,-5,20],2))