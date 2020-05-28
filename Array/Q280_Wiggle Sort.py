
# 思路: 一遍loop, 只要相邻两个数字的关系不符合条件, 交换即可, 不会对之前的关系产生影响

class Solution:
    def wiggleSort(self, nums):
        x = 1
        for i in range(len(nums) - 1):
            if (nums[i] - nums[i + 1]) * x > 0:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
            x = -x
        return nums


a=Solution()
print(a.wiggleSort([3,5,2,1,6,4]))