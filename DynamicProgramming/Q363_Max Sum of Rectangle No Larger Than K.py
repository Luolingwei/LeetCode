
# 思路: 只在行上进行累加, 固定两个列i,j之后，变成一维数组问题
# maximum subarray no larger than k, 用binary search preSum解决，找到不小于curs-k的preS

import bisect
class Solution:
    def maxSumSubmatrix(self, matrix, k):
        def helper(nums, k):
            memo = [float('inf')]
            curs, ans = 0, float('-inf')
            for n in nums:
                bisect.insort(memo, curs)
                curs += n
                i = bisect.bisect_left(memo, curs - k)
                ans = max(ans, curs - memo[i])
            return ans

        m, n = len(matrix), len(matrix[0])
        res = float('-inf')
        for row in matrix:
            for j in range(1, n):
                row[j] += row[j - 1]
        for i in range(n):
            for j in range(-1, i):
                res = max(res, helper([matrix[k][i] - (matrix[k][j] if j >= 0 else 0) for k in range(m)], k))
        return res