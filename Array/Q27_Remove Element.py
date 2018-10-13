class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i=0
        l=len(nums)
        while i<l:
            if nums[i]==val:
                nums.pop(i)
                l=l-1
            else:
                i = i + 1
        new_l=len(nums)
        return new_l

a=Solution()
print(a.removeElement([0,1,1,2,2,3,3,4,4,4,5],0))