class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=1
        if nums==[]:
            return 0
        l=len(nums)
        index=nums[0]
        while i<l:
            if nums[i]==index:
                nums.pop(i)
                l=l-1
            else:
                index=nums[i]
                i = i + 1
        new_l=len(nums)
        return new_l

a=Solution()
print(a.removeDuplicates([0,0,1,1,2,2,3,3,3,5,6,6]))
print(a.removeDuplicates([0,1,1,1,1,3,3,3]))