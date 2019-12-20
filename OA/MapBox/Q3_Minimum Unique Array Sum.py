class Solution:
    def find(self,nums):
        nums.sort()
        for i in range(1,len(nums)):
            if nums[i]<=nums[i-1]:
                nums[i]=nums[i-1]+1
        return sum(nums)

a=Solution()
print(a.find([3,2,1,2,7]))
print(a.find([1,2,2]))