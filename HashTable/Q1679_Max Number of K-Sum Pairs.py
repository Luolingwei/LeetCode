from collections import Counter

# 思路: 用memo记录已经有的数字个数, 碰到k-n就匹配一对, 数字个数减1

class Solution:
    def maxOperations(self, nums, k):
        memo = Counter()
        res = 0
        for n in nums:
            if memo[k - n] > 0:
                res += 1
                memo[k - n] -= 1
            else:
                memo[n] += 1
        return res


a=Solution()
print(a.maxOperations([1,2,3,4],5))
print(a.maxOperations([3,1,3,4,3],6))