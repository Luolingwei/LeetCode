class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        j=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[i],nums[j]=nums[j],nums[i]
                j+=1
        return nums

a=Solution()
print(a.moveZeroes([0,1,0,3,12]))
print(a.moveZeroes([0,1,0,3,0,2,10,0]))
print(a.moveZeroes([0,1,0]))