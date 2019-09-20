
# 和Q33不同的是，当nums[mid]==nums[r]时候，需要用r-=1进行缩小范围，因为无法确定左边已排序还是右边已排序

class Solution:
    def search(self, nums, target):
        l,r=0,len(nums)-1
        while l<=r:
            mid=(l+r)//2
            if nums[mid]==target: return True
            if nums[mid]>nums[r]:
                if nums[l]<=target<nums[mid]:
                    r=mid-1
                else:
                    l=mid+1
            elif nums[mid]<nums[r]:
                if nums[mid]<target<=nums[r]:
                    l=mid+1
                else:
                    r=mid-1
            else:
                r-=1
        return False


a=Solution()
print(a.search([2,5,6,0,0,1,2],0))
print(a.search([2,5,6,0,0,1,2],3))
print(a.search([1],3))
print(a.search([1,2],3))