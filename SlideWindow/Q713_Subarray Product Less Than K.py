# Input: nums = [10, 5, 2, 6], k = 100
# Output: 8
# Explanation: The 8 subarrays that have product less than 100 are: [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6].
# Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.

# 思路1: 用dp先计算累积乘积，然后统计不同起点和终点subarray的乘积.
# 思路2: sliding window, 设置left为0，每来一个数字，累乘，如果乘积大于k，从左边去掉因子，直到sum<k，此时以该数结尾的子数组有i-l+1个

class Solution:
    # Solution 1 dp TLE
    # def numSubarrayProductLessThanK(self, nums, k):
    #     A=[1]+nums
    #     N,ans=len(A),0
    #     for i in range(1,N):
    #         A[i]*=A[i-1]
    #     for i in range(N-1):
    #         for j in range(i+1,N):
    #             if A[j]//A[i]<k:
    #                 ans+=1
    #             else:
    #                 break
    #     return ans

    # Solution 2 sliding window
    def numSubarrayProductLessThanK(self, nums, k):
        l,curS,ans=0,1,0
        for i in range(len(nums)):
            curS*=nums[i]
            while l<i and curS>=k:
                curS,l=curS//nums[l],l+1
            if curS<k: ans+=i-l+1
        return ans

a=Solution()
print(a.numSubarrayProductLessThanK([10, 5, 2, 6],100))
print(a.numSubarrayProductLessThanK([1, 2, 3, 4],3))
print(a.numSubarrayProductLessThanK([5,2,3],1))
print(a.numSubarrayProductLessThanK([1,2,3],0))