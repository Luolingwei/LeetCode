class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low=0
        high=len(nums)-1
        while low<high:
            mid=(low+high)//2
            if nums[mid]>nums[high]:
                low=mid+1
            else:
                high=mid
        return nums[high]

a=Solution()
print(a.findMin([3,4,5,1,2]))
print(a.findMin([4,5,6,7,0,1,2]))