# Input: [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

# 思路 1: dp, dp[i]表示以i结尾的最长递增数组长度，dp[i]=max(dp[j]+1 if nums[i]>nums[j], j从0到i)
# 思路 2: bisect，每来一个数字，寻找其在数组中的位置，如果位置是末尾，则加入数组，否则将相应位置的数字替换为该数字（更小）

import bisect
class Solution:

    # Solution 1 dp 1144 ms
    # def lengthOfLIS(self, nums):
    #     dp=[1]*len(nums)
    #     for j in range(len(nums)):
    #         for i in range(j):
    #             if nums[j]>nums[i]:
    #                 dp[j]=max(dp[j],dp[i]+1)
    #     return max(dp or [0])

    # Solution 2 bisect 40 ms
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp=[]
        for num in nums:
            bi=bisect.bisect_left(dp,num)
            if bi==len(dp):
                dp+=[num]
            else:
                dp[bi]=num
        return len(dp)

a=Solution()
print(a.lengthOfLIS([10,9,2,5,3,8,101,6,7]))
print(a.lengthOfLIS([1,1,1,1]))