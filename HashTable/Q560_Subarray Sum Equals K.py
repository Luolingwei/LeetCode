
# HashTable记录每个每个数字结尾的curS，统计presum个数，count[curS-k]为以每个数字结尾的sumK数组个数

class Solution:
    def subarraySum(self, nums, k):
        dic={0:1}
        ans=pre_sum=0
        for num in nums:
            pre_sum+=num
            ans+=dic.get(pre_sum-k,0)
            dic[pre_sum]=dic.get(pre_sum,0)+1
        return ans

a=Solution()
print(a.subarraySum([1,3,5,7,1,2,3,2,9],3))
print(a.subarraySum([1,1,1],2))
print(a.subarraySum([1],0))