class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i=0
        zero_index=0
        two_index=len(nums)-1

        while i<two_index+1:
            if nums[i]==0:
                nums[zero_index],nums[i]=nums[i],nums[zero_index]
                zero_index+=1
                i+=1
            elif nums[i]==2:
                nums[two_index],nums[i]=nums[i],nums[two_index]
                two_index-=1
            else:
                i+=1
        return nums

a=Solution()
print(a.sortColors([2,0,2,1,1,0]))
print(a.sortColors([0,1,0,2,0]))
