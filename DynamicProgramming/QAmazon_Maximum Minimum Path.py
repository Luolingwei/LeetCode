# [8, 4, 7]
# [6, 5, 9]
# 有3条path：
# 8-4-7-9 min: 4
# 8-4-5-9 min: 4
# 8-6-5-9 min: 5
# return: 5

# 思路: 对于dp[i][j]，其最大的min=min(matrix[i][j],max(dp[i-1][j],dp[i][j-1])) (保证之前的min值尽量大)

class Solution:
    def Maxmin(self,matrix):
        m,n=len(matrix),len(matrix[0])
        for i in range(m):
            for j in range(n):
                if i+j==0: continue
                a,b=float('-inf'),float('-inf')
                if i-1>=0: a=matrix[i-1][j]
                if j-1>=0: b=matrix[i][j-1]
                matrix[i][j]=min(matrix[i][j],max(a,b))
        return matrix[-1][-1]

a=Solution()
print(a.Maxmin([[8, 4, 7],[6, 5, 9]]))