# Input: matrix = [[1,-1],[-1,1]], target = 0
# Output: 5
# Explanation: The two 1x2 submatrices, plus the two 2x1 submatrices, plus the 2x2 submatrix.

# 思路: 常规解法dp计算左上角的矩阵之和，需要O(n^4)
# 这里只在行上进行累加, 固定行之后，依次从上往下累加列，并用dic记录cursum，dic[cursum-target]即构成sumtarget的矩阵数量.

class Solution:
    def numSubmatrixSumTarget(self, matrix, target):
        m,n,ans=len(matrix),len(matrix[0]),0
        for row in matrix:
            for j in range(1,n):
                row[j]+=row[j-1]
        for i in range(n):
            for j in range(-1,i):
                cursum,dic=0,{0:1}
                for k in range(m):
                    cursum+=matrix[k][i]-(matrix[k][j] if j>=0 else 0)
                    ans+=dic.get(cursum-target,0)
                    dic[cursum]=dic.get(cursum,0)+1
        return ans

a=Solution()
print(a.numSubmatrixSumTarget([[1,-1],[-1,1]],0))
print(a.numSubmatrixSumTarget([[0,1,0],[1,1,1],[0,1,0]],0))