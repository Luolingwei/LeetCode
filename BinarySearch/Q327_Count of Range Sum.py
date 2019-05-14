# Input: nums = [-2,5,-1], lower = -2, upper = 2,
# Output: 3
# Explanation: The three ranges are : [0,0], [2,2], [0,2] and their respective sums are: -2, -1, 2.

# 思路: 依次加入n，以array的顺序更新dp_sum，每更新一次dp_sum，增加的数量为满足lower<=thisSum-preSum<=upper的presum个数。即thisSum-upper<=preSum<=thisSum-lower的个数，每次将thisSum按顺序存储，方便找出在范围内的个数。

import bisect
class Solution:
    def countRangeSum(self, nums, lower, upper):
        preSum,thisSum,ans=[0],0,0
        for n in nums:
            thisSum+=n
            ans+=bisect.bisect_right(preSum,thisSum-lower)-bisect.bisect_left(preSum,thisSum-upper)
            bisect.insort(preSum,thisSum)
        return ans

a=Solution()
print(a.countRangeSum([-2,5,-1],-2,2))
print(a.countRangeSum([-2,1,2],-2,2))