
# 思路: 固定左边的sum, 那么中间的sum最低为left_sum, 最高为剩下的total//2
# 用二分确定符合条件的中间数组的分界范围
# O(nlogn)

import bisect
class Solution:
    def waysToSplit(self, nums):
        total, L = sum(nums), len(nums)
        preS = nums[:]
        for i in range(1,L): preS[i] += preS[i - 1]

        left, res, mod = 0, 0, 10**9+7
        for i, n in enumerate(nums):
            left += n
            total -= n
            low, high = 2*left, left + total//2
            if low>high: break
            low_idx = bisect.bisect_left(preS, low)
            high_idx = bisect.bisect_right(preS, high)-1
            res += max(0, min(L-2, high_idx) - max(i+1,low_idx) + 1)
        return res%mod


a=Solution()
print(a.waysToSplit([1,1,1]))
print(a.waysToSplit([1,2,2,2,5,0]))
print(a.waysToSplit([3,2,1]))
print(a.waysToSplit([0,3,3]))
print(a.waysToSplit([2,8,10,0,2]))
print(a.waysToSplit([0,0,0]))