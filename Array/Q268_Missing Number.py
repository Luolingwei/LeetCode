class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return int((len(nums)*len(nums)+len(nums))/2-sum(nums))

a=Solution()
print(a.missingNumber([3,0,1]))
print(a.missingNumber([9,6,4,2,3,5,7,0,1]))