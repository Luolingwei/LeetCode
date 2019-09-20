# Input:
# nums = [1, 7, 3, 6, 5, 6]
# Output: 3
# Explanation:
# The sum of the numbers to the left of index 3 (nums[3] = 6) is equal to the sum of numbers to the right of index 3.
# Also, 3 is the first index where this occurs.

# 思路: 如果(totalS-n)/2==preS，那么说明左右两边总和相等

class Solution:
    def pivotIndex(self, nums):
        total=sum(nums)
        pre=0
        for i,n in enumerate(nums):
            if (total-n)/2==pre:
                return i
            pre+=n
        return -1

a=Solution()
print(a.pivotIndex([1, 7, 3, 6, 5, 6]))