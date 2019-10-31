# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.

# 思路: dp[i]表示以i结尾的最大subarray，可以改为O(1)space

class Solution:
    # 1 return maxSum
    # def maxSubArray(self, nums):
    #     N,ans=len(nums),nums[0]
    #     dp=nums[0]
    #     for i in range(1,N):
    #         dp=max(dp+nums[i],nums[i])
    #         ans=max(ans,dp)
    #     return ans

    # follow up: return indexes
    def maxSubArray(self, nums):
        N=len(nums)
        ans=nums[0]
        ansl,ansr=0,0
        left,right=0,0
        for i in range(1,N):
            if nums[i-1]>0:
                right=i
                nums[i]+=nums[i-1]
            else:
                left=right=i
            if nums[i]>ans:
                ans=nums[i]
                ansl,ansr=left,right
        return ans,ansl,ansr

a = Solution()
print(a.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(a.maxSubArray([-1,-2,-3]))
print(a.maxSubArray([-1,6,-3,5,-6,-10,6,7,6,-10,12]))
print(a.maxSubArray([-1,-3,-5,-2]))
print(a.maxSubArray([1,2,3,4]))
print(a.maxSubArray([-4,-3,-1,-2]))