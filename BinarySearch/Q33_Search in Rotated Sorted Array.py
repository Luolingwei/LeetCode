# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4

# 思路: binary search，需要根据nums[mid]和两边值的大小判断哪边是排序好的.然后根据target是否在范围内缩小查找范围.

class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l,r=0,len(nums)-1
        while l<=r:
            mid=(l+r)//2
            if nums[mid]==target: return mid
            if nums[l]<=nums[mid]: # 左边是排序好的
                if nums[l]<=target<nums[mid]:
                    r=mid-1
                else:
                    l=mid+1
            else:
                if nums[mid]<target<=nums[r]: #右边是排序好的
                    l=mid+1
                else:
                    r=mid-1
        return -1

a=Solution()
print(a.search([4,5,6,7,0,1,2],1))
print(a.search([4,5,6,7,0,1,2],6))
print(a.search([4,5,6,7,0,1,2],9))
print(a.search([1,3],2))
print(a.search([3,2,1],3))
print(a.search([3,1],1))