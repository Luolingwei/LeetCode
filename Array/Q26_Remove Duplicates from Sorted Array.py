class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)-1,0,-1):
            if nums[i]==nums[i-1]:
                nums.pop(i)
        return len(nums)

a=Solution()
print(a.removeDuplicates([0,0,1,1,2,2,3,3,3,5,6,6]))
print(a.removeDuplicates([0,1,1,1,1,3,3,3]))