class Solution:
    def getRange(self,nums,center):
        left,right=center,center
        while left>-1 and nums[left]==nums[center]: left-=1
        while right<len(nums) and nums[right]==nums[center]: right+=1
        return [left+1,right-1]

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        low,high=0,len(nums)-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]==target:
                return self.getRange(nums,mid)
            elif nums[mid]>target:
                high=mid-1
            else:
                low=mid+1
        return [-1,-1]

a=Solution()
print(a.searchRange([1,4,6],4))
print(a.searchRange([1,4,4,4,4,4,4],4))
print(a.searchRange([4,4,4,4,4,4,1,1],4))
print(a.searchRange([4,5,5,5,5,6,7],5))
print(a.searchRange([1,5,6,7,8,9,10],6))
print(a.searchRange([4,5],6))
print(a.searchRange([],6))