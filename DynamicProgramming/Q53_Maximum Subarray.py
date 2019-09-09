# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.

# 思路: dp[i]表示以i结尾的最大subarray，可以改为O(1)space

class Solution:
    def maxSubArray(self, nums):
        N,ans=len(nums),nums[0]
        dp=nums[0]
        for i in range(1,N):
            dp=max(dp+nums[i],nums[i])
            ans=max(ans,dp)
        return ans

a = Solution()
print(a.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(a.maxSubArray([-1,-2,-3]))