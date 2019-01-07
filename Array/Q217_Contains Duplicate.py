class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(nums)!=len(set(nums))

a=Solution()
print(a.containsDuplicate([1,2,3,1]))
print(a.containsDuplicate([1,2,3,4]))