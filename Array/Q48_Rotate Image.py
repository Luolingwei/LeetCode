
# Common method:
# 顺时针: 先上下reverse，然后交换非对角线的对称元素
# 顺时针: 先左右reverse，然后交换非对角线的对称元素

class Solution:
    # 顺时针
    # def rotate(self, matrix):
    #     N=len(matrix)
    #     matrix[:]=matrix[::-1]
    #     for i in range(N):
    #         for j in range(i+1,N):
    #             matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
    #         return matrix

    # 逆时针
    def rotate(self, matrix):
        N=len(matrix)
        for i in range(N):
            l,r=0,N-1
            while l<r:
                matrix[i][l],matrix[i][r]=matrix[i][r],matrix[i][l]
                l+=1
                r-=1
        for i in range(N):
            for j in range(i+1,N):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        return matrix

a = Solution()
print(a.rotate([[1,2,3],[4,5,6],[7,8,9]]))