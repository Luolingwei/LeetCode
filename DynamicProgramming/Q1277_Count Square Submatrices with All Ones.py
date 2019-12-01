
# 思路: 和Q221一样，以每个像素作为右下角的正方形个数 = 以该像素为右下角的最大正方形边长
# 对矩阵求和即可，Q221为求max

class Solution:
    def countSquares(self, matrix):
        m,n=len(matrix),len(matrix and matrix[0])
        if not m or not n: return 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j]*i*j:
                    matrix[i][j]=min(matrix[i-1][j],matrix[i][j-1],matrix[i-1][j-1])+1
        return sum(map(sum,matrix))