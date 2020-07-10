
# 思路: 对于1D array，计算连续的1即可, 对于2D array, 设置行上限和下线, 从上到下对每一列的数字&
# 即当前所有列都为1才行, 然后当做1D array计算

class Solution:

    def count_1D(self, nums):
        l, total = 0, 0
        for n in nums:
            if n:
                l += 1
            else:
                l = 0
            total += l
        return total

    def numSubmat(self, arr):
        m, n = len(arr), len(arr[0])
        res = 0
        for i in range(m):
            preMemo = [1] * n
            for j in range(i, m):
                for k in range(n): preMemo[k] &= arr[j][k]
                res += self.count_1D(preMemo)
        return res

a=Solution()
print(a.count_1D([[1,0,1],[1,1,0],[1,1,0]]))
print(a.count_1D([[0,1,1,0],[0,1,1,1],[1,1,1,0]]))