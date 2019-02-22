class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i=len(nums)-1
        while i>0 and nums[i]<=nums[i-1]:
            i-=1
        if i==0: nums.sort()
        else:
            temp=len(nums)-1
            while nums[temp]<=nums[i-1]:
                temp-=1
            nums[temp],nums[i-1]=nums[i-1],nums[temp]
            k=len(nums)-1
            while i<k:
                nums[i],nums[k]=nums[k],nums[i]
                i,k=i+1,k-1

a=Solution()
print(a.nextPermutation([1,5,2,4,3,3,2]))
print(a.nextPermutation([1,3,4,2,8,5]))
print(a.nextPermutation([2,1,1,3]))
print(a.nextPermutation([3,2,1]))