
# 思路: 总和加起来最大为2^21, 所以对每个遇到的数寻找可以配对的数即可, sum 从2^0 ~ 2^21
# O(22N)

from collections import Counter
class Solution:
    def countPairs(self, deliciousness):
        memo = Counter()
        res, mod = 0, 10**9+7
        for n in deliciousness:
            for p in range(22):
                target = 2**p
                res += memo[target-n]
            memo[n] += 1
        return res%mod


a=Solution()
print(a.countPairs([1,3,5,7,9]))
print(a.countPairs([1,1,1,3,3,3,7]))