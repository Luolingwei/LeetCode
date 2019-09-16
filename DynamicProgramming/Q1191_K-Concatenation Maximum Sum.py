# Input: arr = [1,2], k = 3
# Output: 9

# Input: arr = [-1,-2], k = 7
# Output: 0

# 思路: 因为是repeated数组
# 如果数组sum>0，那么res=中间的k-2个sum加起来+首尾两个的最大subarray(一定能连起来，因为sum>0)
# 如果数组sum<0，那么res=两个array连起来的最大subarray

class Solution:
    def kConcatenationMaxSum(self, arr, k):
        def helper(nums):
            maxS,curS=nums[0],nums[0]
            for i in range(1,len(nums)):
                curS=max(nums[i],curS+nums[i])
                maxS=max(maxS,curS)
            return max(0,maxS)
        T,mod=sum(arr),10**9+7
        return (helper(arr*2)+max(0,T)*(k-2))%mod if k>1 else helper(arr)%mod

a=Solution()
print(a.kConcatenationMaxSum([1,2],3))
print(a.kConcatenationMaxSum([1,-2,1],5))
print(a.kConcatenationMaxSum([-1,-2],7))