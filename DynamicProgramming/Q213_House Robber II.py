class Solution:
    def rob(self, nums):
        if len(nums)<2:
            return 0 if not nums else nums[0]
        #money1第一个闲置 money2第一个偷
        money1,money2=[0]*len(nums),[0]*len(nums)
        money1[1]=nums[1]
        money2[0],money2[1]=nums[0],nums[0]
        for i in range(2,len(nums)):
            money1[i]=max(money1[i-1],money1[i-2]+nums[i])
            money2[i]=max(money2[i-1],money2[i-2]+nums[i])
            if i==len(nums)-1: money2[i]=money2[i-1]
        return max(money1[-1],money2[-1])

a=Solution()
print(a.rob([1,2,3,1]))
print(a.rob([2,3,2]))