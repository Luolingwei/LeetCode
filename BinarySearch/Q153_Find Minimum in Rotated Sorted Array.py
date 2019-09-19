
# 思路1: 用nums[mid]和nums[r]的大小关系判断最小值所落在的区间.
# 思路2: divide and conquer, 分成左右两个数组，分别考虑是否递增(必有一个递增)

class Solution:
    # Solution 1 binary search
    def findMin(self, nums):
        l,r=0,len(nums)-1
        while l<r:
            mid=(l+r)//2
            if nums[mid]>nums[r]:
                l=mid+1
            else:
                r=mid
        return nums[l]

    # Solution 2 divide and conquer
    # def findMin(self, nums):
    #     if len(nums)<=2: return min(nums)
    #     if nums[0]<nums[-1]: return nums[0]
    #     mid=len(nums) // 2
    #     return min(self.findMin(nums[:mid]),self.findMin(nums[mid:]))


a=Solution()
print(a.findMin([3,4,5,1,2]))
print(a.findMin([4,5,6,7,0,1,2]))