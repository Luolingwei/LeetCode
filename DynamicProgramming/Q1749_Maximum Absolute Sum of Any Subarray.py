
# 思路: 计算最大sum子数组和最小sum子数组即可

class Solution:
    def maxAbsoluteSum(self, nums) -> int:
        minN, maxN = 0, 0
        res = 0
        for n in nums:
            maxN = max(0, maxN) + n
            minN = min(0, minN) + n
            res = max(res, maxN, -minN)
        return res


a=Solution()
print(a.maxAbsoluteSum([0,0,0]))
print(a.maxAbsoluteSum([1]))
print(a.maxAbsoluteSum([1,-3,2,3,-4]))
print(a.maxAbsoluteSum([2,-5,1,-4,3,-2]))