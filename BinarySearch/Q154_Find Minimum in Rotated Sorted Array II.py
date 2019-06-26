
# 思路: 这里有重复值出现，当nums[mid]==nums[r]时，用r-=1处理重复值.

class Solution:
    def findMin(self, nums):
        l,r=0,len(nums)-1
        while l<r:
            mid=(l+r)//2
            if nums[mid]>nums[r]:
                l=mid+1
            elif nums[mid]==nums[r]:
                r-=1
            else:
                r=mid
        return nums[l]

a = Solution()
print(a.findMin([4,5,6,7,0,1,2]))
print(a.findMin([2,2,2,2,3,4,5,0,1]))
print(a.findMin([6,7,8,1,3,6]))
print(a.findMin([3,3,3,3,3,1,2,3]))
print(a.findMin([4,5,6,3,3,3,3,3,3,3]))
print(a.findMin([5,3,3,3,3,3]))