class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # if len(nums)==1:
        #     return 0
        # for i in range(len(nums)):
        #     if i==0:
        #         if nums[i]>nums[i+1]:
        #             return i
        #     if i==len(nums)-1:
        #         if nums[i]>nums[i-1]:
        #             return i
        #     if nums[i]>nums[i-1] and nums[i]>nums[i+1]:
        #         return i

        low = 0
        high = len(nums) - 1

        while low < high:
            mid = (low + high) // 2
            if nums[mid] > nums[mid + 1] and nums[mid] > nums[mid - 1]:
                return mid
            elif nums[mid] < nums[mid + 1]:
                low = mid + 1
            else:
                high = mid - 1
        return low

a=Solution()
print(a.findPeakElement([1]))

