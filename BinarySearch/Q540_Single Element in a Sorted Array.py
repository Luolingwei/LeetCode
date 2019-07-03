# Input: [1,1,2,3,3,4,4,8,8]
# Output: 2

# 思路: 二分查找，因为数组肯定是奇数个，而且单个数字肯定存在奇数的一半中，根据截取的array的长度奇偶 和 mid的相邻相等关系判断target落在的区间.

class Solution:
    def singleNonDuplicate(self, nums):
        l,r=0,len(nums)-1
        while l<r:
            mid=(l+r)//2
            if (mid-l)%2==0:# mid及左边是奇数个
                if nums[mid]==nums[mid-1]:
                    r=mid-2
                else:
                    if nums[mid]!=nums[mid+1]:
                        return nums[mid]
                    l=mid+2
            else: # mid及左边是偶数个
                if nums[mid]==nums[mid-1]:
                    l=mid+1
                else:
                    r=mid-1
        return nums[l]

a=Solution()
print(a.singleNonDuplicate([1,1,2,3,3,4,4,8,8]))
print(a.singleNonDuplicate([3,3,7,7,10,11,11]))
print(a.singleNonDuplicate([1,1,2,2,3]))