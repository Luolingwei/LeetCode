# Given nums = [3,2,2,3], val = 3,
#
# Your function should return length = 2, with the first two elements of nums being 2.
#
# It doesn't matter what you leave beyond the returned length.
# modifying the input array in-place with O(1) extra memory.

class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i,l=0,len(nums)
        while i<l:
            if nums[i]==val:
                nums.pop(i)
                l=l-1
            else:
                i=i+1
        return l

a=Solution()
print(a.removeElement([0,1,1,2,2,3,3,4,4,4,5],0))