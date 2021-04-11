
# 思路: 寻找最左边>=target的位置 和 最右边<=target的位置

class Solution:
    def searchRange(self, nums, target):
        if not nums: return [-1, -1]
        return [self.search_left(nums, target), self.search_right(nums, target)]

    def search_left(self, nums, target):
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid
        return l if nums[l] == target else -1

    def search_right(self, nums, target):
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r + 1) // 2
            if nums[mid] > target:
                r = mid - 1
            else:
                l = mid
        return l if nums[l] == target else -1


a=Solution()
print(a.searchRange([1,4,6],4))
print(a.searchRange([1,4,4,4,4,4,4],4))
print(a.searchRange([4,4,4,4,4,4],4))
print(a.searchRange([4,5,5,5,5,6,7],5))
print(a.searchRange([1,5,6,7,8,9,10],6))
print(a.searchRange([4,5],6))
print(a.searchRange([],6))