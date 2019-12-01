
# 思路: 考虑左边和右边的最大正方形，取min，然后还要左上角填充，故取三者的最小值+1作为以当前元素作为右下角的最大正方形边长

class Solution:
    def maximalSquare(self, matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j]=int(matrix[i][j])
                if matrix[i][j]*i*j:
                    matrix[i][j]=min(matrix[i-1][j],matrix[i][j-1],matrix[i-1][j-1])+1
        return len(matrix) and max(map(max,matrix))**2
