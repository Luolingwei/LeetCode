class Solution:
    def construct(self,nums):
        x=-1
        for i in range(len(nums)-1):
            if (nums[i]-nums[i+1])*x<0:
                nums[i],nums[i+1]=nums[i+1],nums[i]
            x=-x
        return nums

a=Solution()
print(a.construct([6,2,7,1,4,5,9]))
print(a.construct([5,6,3,4,2,1]))
print(a.construct([5,3,4,1,6,2]))