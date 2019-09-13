import bisect
class Solution:
    # Solution 1 bisect
    # def searchInsert(self, nums, target):
    #     return bisect.bisect_left(nums,target)

    # Solution 2 binary search
    # 寻找第一个大于等于target的数
    # def searchInsert(self, nums, target):
    #     l,r=0,len(nums)
    #     while l<r:
    #         mid=(l+r)//2
    #         if nums[mid]<target: l=mid+1
    #         else: r=mid
    #     return l

    # 寻找小于等于target的最大数
    def searchInsert(self, nums, target):
        l,r=0,len(nums)-1
        while l<r:
            mid=(l+r+1)//2
            if nums[mid]>target: r=mid-1
            else: l=mid
        return l


a=Solution()
print(a.searchInsert([],1))
print(a.searchInsert([1,3],2))
print(a.searchInsert([1],0))
print(a.searchInsert([1,4,6],7))
print(a.searchInsert([1,3,4,6,7,8,9],5))
print(a.searchInsert([1,2,3,4,5,7,8,9],7))