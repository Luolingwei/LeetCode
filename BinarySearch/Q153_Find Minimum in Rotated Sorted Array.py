
# 思路: 用nums[mid]和nums[r]的大小关系判断最小值所落在的区间.

class Solution:
    def findMin(self, nums):
        l,r=0,len(nums)-1
        while l<r:
            mid=(l+r)//2
            if nums[mid]>nums[r]:
                l=mid+1
            else:
                r=mid
        return nums[l]

a=Solution()
print(a.findMin([3,4,5,1,2]))
print(a.findMin([4,5,6,7,0,1,2]))