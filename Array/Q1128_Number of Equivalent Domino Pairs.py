# Input: dominoes = [[1,2],[2,1],[3,4],[5,6]]
# Output: 1

# 思路: 将每个数对排序，count相同的数对，最后计算可以构成pair的数量

import collections
class Solution:
    def numEquivDominoPairs(self, dominoes):
        d=[tuple(sorted(sub)) for sub in dominoes]
        c=collections.Counter(d)
        return sum(n*(n-1)//2 for n in c.values())

a=Solution()
print(a.numEquivDominoPairs([[1,2],[2,1],[3,4],[5,6]]))