
# 思路: 题目转化为寻找中间的最大的sum为sum_nums-x的子数组
# sliding window 或者 preSum memo

class Solution:

    # preSum memo
    def minOperations(self, nums, x):
        memo = {0:-1}
        curs, sum_nums = 0, sum(nums)
        max_window, target = 0, sum_nums - x
        if target == 0: return len(nums)
        for i,n in enumerate(nums):
            curs += n
            memo[curs] = i
            if curs - target in memo:
                max_window = max(max_window, i - memo[curs - target])
        return len(nums) - max_window if max_window>0 else -1

    # sliding window
    def minOperations2(self, nums, x):
        l, max_window = 0, 0
        curs, target = 0, sum(nums) - x
        if target == 0: return len(nums)
        if target < 0: return -1
        for r, n in enumerate(nums):
            curs += nums[r]
            while curs>=target:
                if curs == target:
                    max_window = max(max_window, r-l+1)
                curs -= nums[l]
                l+=1
        return len(nums) - max_window if max_window>0 else -1


a=Solution()
print(a.minOperations([1,1,4,2,3],5))
print(a.minOperations([5,6,7,8,9],4))
print(a.minOperations([3,2,20,1,1,3],10))
print(a.minOperations([1,1,3,2,5],5))
print(a.minOperations([1,1],2))
print(a.minOperations([1,1],3))