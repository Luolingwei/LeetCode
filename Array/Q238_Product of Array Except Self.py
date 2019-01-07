class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans=[1]*len(nums)
        pre=after=1
        for i in range(1,len(nums)):
            pre=pre*nums[i-1]
            ans[i]=ans[i]*pre
        for j in range(len(nums)-2,-1,-1):
            after=after*nums[j+1]
            ans[j]=ans[j]*after
        return ans

a=Solution()
print(a.productExceptSelf([1,2,3,4]))