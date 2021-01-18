
# 思路: 先计算出每个column连续1的最长长度
# 考虑某一行从前往后，需要 横向长度*column连续1的最小值
# 所以将每一行可以实现的最长1降序排列, 即每个点可以实现的最长1的column序列
# 扫描每一行, 用横向长度乘以最长column长度, 取max即可

class Solution:
    def largestSubmatrix(self, matrix):
        m,n = len(matrix), len(matrix[0])
        memo = [[0]*n for _ in range(m)]
        for j in range(n):
            for i in range(m):
                if matrix[i][j]==1:
                    memo[i][j]=memo[i-1][j]+1
        for row in memo: row.sort(reverse=True)
        res = 0
        for i in range(m):
            for j in range(n):
                maxCL = memo[i][j]
                res = max(res,(j+1)*maxCL)
        return res


a=Solution()
print(a.largestSubmatrix([[0,0,1],[1,1,1],[1,0,1]]))
print(a.largestSubmatrix([[1,0,1,0,1]]))
print(a.largestSubmatrix([[1,1,0],[1,0,1]]))
print(a.largestSubmatrix([[0,0],[0,0]]))