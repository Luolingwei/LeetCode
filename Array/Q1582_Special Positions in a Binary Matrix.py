
# 思路: 先计算行sum和列sum, 如果mat[i][j]==1而且当前行列的sum都是1, 则说明当前行和列只有它一个1

class Solution:
    def numSpecial(self, mat):
        m, n = len(mat), len(mat[0])
        rowS = [sum(row) for row in mat]
        colS = [sum(col) for col in zip(*mat)]
        res = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1 and rowS[i] == 1 and colS[j] == 1:
                    res += 1
        return res

a=Solution()
print(a.numSpecial([[1,0,0],[0,0,1],[1,0,0]]))
print(a.numSpecial([[1,0,0],[0,1,0],[0,0,1]]))