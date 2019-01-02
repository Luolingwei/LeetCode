class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(1,len(nums)):
            if nums[i]<nums[i-1]:
                return nums[i]
        return nums[0]

a = Solution()
print(a.findMin([4,5,6,7,0,1,2]))
print(a.findMin([2,2,2,2,3,4,5,0,1]))
print(a.findMin([6,7,8,1,3,6]))
print(a.findMin([1,3,3]))