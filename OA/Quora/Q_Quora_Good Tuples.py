class Solution:
    def find(self,nums):
        ans=0
        for i in range(1,len(nums)-1):
            if len({nums[i-1],nums[i],nums[i+1]})==3:
                ans+=1
        return ans

a=Solution()
print(a.find([1, 1, 2, 1, 5, 3, 2, 3]))