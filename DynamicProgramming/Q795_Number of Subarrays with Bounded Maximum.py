# Example :
# Input:
# A = [2, 1, 4, 3]
# L = 2
# R = 3
# Output: 3
# Explanation: There are three subarrays that meet the requirements: [2], [2, 1], [3].

# 思路: 用prev记录小于R的连续数组的最左边坐标, dp[i]记录以i结尾的数组个数，当L<=num<=R时，dp[i]=i-prev，当num<L时，dp[i]不变，当num>R时，dp[i]=0（同时prev=i）

class Solution:
    # Solution 1 O(n) time O(n) Space
    # 88 ms, 14.5 MB
    # def numSubarrayBoundedMax(self, A, L, R):
    #     prev,dp=-1,[0]*len(A)
    #     for i,num in enumerate(A):
    #         if L<=num<=R:
    #             dp[i]=i-prev
    #         if num>R:
    #             dp[i],prev=0,i
    #         if num<L:
    #             dp[i]=dp[i-1]
    #     return sum(dp)

    # Solution 2 O(n) time O(1) Space
    #  84 ms, 14.3 MB
    def numSubarrayBoundedMax(self, A, L, R):
        prev,ans,dp=-1,0,0
        for i,num in enumerate(A):
            if L<=num<=R:
                dp=i-prev
            if num>R:
                dp,prev=0,i
            ans+=dp
        return ans

a=Solution()
print(a.numSubarrayBoundedMax([2, 1, 4, 3], 2, 3))
print(a.numSubarrayBoundedMax([2, 1, 4, 3, 5, 2, 3, 4, 1], 2, 3))
print(a.numSubarrayBoundedMax([2], 2, 3))
print(a.numSubarrayBoundedMax([73,55,36,5,55,14,9,7,72,52], 32, 69))