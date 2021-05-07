
# 思路: 同Q1060, 找到最右边的index使得left_missing个数小于k, 那么再往下一个left_missing就会>=k, 说明missing number就在此number右侧
# return nums[l] + k-(nums[l]-1-l). 如果没有找到left_missing个数小于k小于k的位置，说明所有missing number都大于k, 直接返回k

class Solution:
    def findKthPositive(self, nums, k):
        l, r = 0, len(nums)-1
        while l<r:
            mid = (l+r+1)//2
            left_missing = nums[mid] - 1 - mid
            if left_missing >= k:
                r = mid-1
            else:
                l = mid
        if nums[l]-1-l < k: return nums[l] + k-(nums[l]-1-l)
        else: return k


a=Solution()
print(a.findKthPositive([2,3,4,7,11], 5))
print(a.findKthPositive([3,4,7,11], 1))
print(a.findKthPositive([3,4,7,11], 2))
print(a.findKthPositive([1,2,3,4], 2))