
# 思路: 先计算每一列的最大值，然后排序分配给两人即可

class Solution:
    def MatrixGame(self,matrix):
        m,n=len(matrix),len(matrix[0])
        nums=[max(matrix[i][j] for i in range(m)) for j in range(n)]
        nums.sort(reverse=True)
        return sum(nums[::2])-sum(nums[1::2])

a=Solution()
print(a.MatrixGame([[3,7,5,3,4,5],[4,5,2,6,5,4],[7,4,9,7,8,3]]))