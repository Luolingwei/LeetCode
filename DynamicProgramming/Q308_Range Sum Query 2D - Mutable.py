
# 思路: sumRegion() 和 update() 都有10^4次, 所以不能一个O(mn) 一个 O(1)
# 用每行的preS存储矩阵和
# update时, 更新对应行的preS, O(n)
# sumRegion时, sum row1->row2列对应的preS, O(m)
# 总体实现了均衡

class NumMatrix:

    def __init__(self, matrix):
        m, n = len(matrix), len(matrix[0])
        self.matrix = matrix
        self.preS = [[0] * (n) for _ in range(m)]
        for i in range(m):
            for j in range(n):
                self.preS[i][j] = self.preS[i][j - 1] + matrix[i][j]

    def update(self, row: int, col: int, val: int) -> None:
        for j in range(col, len(self.preS[0])):
            self.preS[row][j] += val - self.matrix[row][col]
        self.matrix[row][col] = val

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = 0
        for i in range(row1, row2 + 1):
            res += self.preS[i][col2] - (self.preS[i][col1 - 1] if col1 > 0 else 0)
        return res


a=NumMatrix([[2,4],[-3,5]])
a.update(0,1,3)
a.update(1,1,-3)
a.update(0,1,1)
print(a.sumRegion(0,0,1,1))