# Input: nums = [1,2,1,3,5,6,4]
# Output: 1 or 5
# Explanation: Your function can return either index number 1 where the peak element is 2,
#              or index number 5 where the peak element is 6.

# 思路: binary search

class Solution:
    def findPeakElement(self, nums):
        l,r=0,len(nums)-1
        while l<r:
            mid=(l+r)//2
            if nums[mid]<nums[mid+1]:
                l=mid+1
            else:
                r=mid
        return l

a=Solution()
print(a.findPeakElement([1]))
print(a.findPeakElement([1,2,1,3,5,6,4]))
print(a.findPeakElement([1,2,3,1]))
