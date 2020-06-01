
# 思路1: 用矩阵乘法进行运算

# 思路2: 考虑到稀疏矩阵的特性, 会有很多0, 所以这里用累加进行运算
# 如果是0, 则不需要累加

class Solution:

    # def multiply(self, A, B):
    #     x,y,z = len(A),len(A[0]),len(B[0])
    #     B = list(zip(*B))
    #     res = [[0]*z for _ in range(x)]
    #     for i in range(x):
    #         for j in range(z):
    #             res[i][j] = sum(A[i][k]*B[j][k] for k in range(y))
    #     return res

    def multiply(self, A, B):
        x, y, z = len(A), len(A[0]), len(B[0])
        res = [[0] * z for _ in range(x)]
        for i in range(x):
            for j in range(y):
                if A[i][j]:
                    for k in range(z):
                        if B[j][k]: res[i][k] += A[i][j] * B[j][k]
        return res


a=Solution()
print(a.multiply([[ 1, 0, 0],[-1, 0, 3]],[[ 7, 0, 0 ],[ 0, 0, 0 ],[ 0, 0, 1 ]]))