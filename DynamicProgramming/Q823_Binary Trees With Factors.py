# Input: A = [2, 4]
# Output: 3
# Explanation: We can make these trees: [2], [4], [4, 2, 2]

# 思路: dp,先将A排序，以每个结点为root的树的构造方法数=其因子的数量之积
# 递推公式: dp[i]=dp[i/j]*dp[j] if i/j and j in list.

import collections
class Solution:
    def numFactoredBinaryTrees(self, A):
        dp=collections.defaultdict(int)
        for n in (sorted(A)):
            dp[n]=1
            for m in dp:
                if n%m==0 and n//m in dp:
                    dp[n]+=dp[n//m]*dp[m]
        return sum(dp.values())%(10**9+7)

a=Solution()
print(a.numFactoredBinaryTrees([2, 4, 5, 10]))
print(a.numFactoredBinaryTrees([2, 4]))