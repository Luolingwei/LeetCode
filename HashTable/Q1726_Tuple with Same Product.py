
# 思路: 由于都是distinct的数字, 统计所有pair乘积出现的次数, 同一个乘积有N个pair那么可搭配出C(N,2)种组合, 最后乘以8即可

from collections import Counter
class Solution:
    def tupleSameProduct(self, nums):
        L, res = len(nums), 0
        memo = Counter()
        for i in range(L):
            for j in range(i+1,L):
                total = nums[i]*nums[j]
                res += 8*memo[total]
                memo[total]+=1
        return res


a=Solution()
print(a.tupleSameProduct([2,3,4,6]))
print(a.tupleSameProduct([1,2,4,5,10]))
print(a.tupleSameProduct([2,3,4,6,8,12]))
print(a.tupleSameProduct([2,3,5,7]))