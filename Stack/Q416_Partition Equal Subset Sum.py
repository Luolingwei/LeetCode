# Input: [1, 5, 11, 5]
#
# Output: true
#
# Explanation: The array can be partitioned as [1, 5, 5] and [11].

# Input: [1, 2, 3, 5]
#
# Output: false
#
# Explanation: The array cannot be partitioned into equal sum subsets.

# 思路(dp): 建立0到target的True False的dp矩阵，每来一个数，更新num到target的状态(因为新加入num之后可能合成数字的范围为num到target)，加完所有数后，返回dp[target].

class Solution:
    # Solution 1: dfs, Time Limit Exceeded
    # def canPartition(self, nums):
    #     def dfs(nums,target):
    #         if target < 0: return
    #         if target == 0: return True
    #         for i in range(len(nums)):
    #             if dfs(nums[i+1:],target-nums[i]):
    #                 return True
    #         return False
    #     total=sum(nums)
    #     if total%2!=0: return False
    #     else: target=total//2
    #     return dfs(nums,target)

    # Solution 2: dp
    def canPartition(self, nums):
        total=sum(nums)
        if total%2!=0: return False
        else: target=total//2
        dp=[True]+[False]*target
        for num in nums:
            for i in range(target,num-1,-1): #避免用到当轮更新的数，所以倒着更新
                dp[i]=dp[i] or dp[i-num]
        return dp[target]


a=Solution()
print(a.canPartition([1, 5, 11, 5]))
print(a.canPartition([1, 2, 3, 5]))
print(a.canPartition([1, 2, 6]))
print(a.canPartition([]))