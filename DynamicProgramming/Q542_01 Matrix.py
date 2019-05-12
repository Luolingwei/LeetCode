# Input:
# [[0,0,0],
#  [0,1,0],
#  [1,1,1]]
#
# Output:
# [[0,0,0],
#  [0,1,0],
#  [1,2,1]]

# 思路: dp，最短距离等于四周的最短距离加一，第一次遍历从左上到右下，得到左上路径的最短距离，此时0仍为0，而1变成了左上的最短距离，再次从右下开始遍历，得到四个方向的最短距离

class Solution:
    def updateMatrix(self, matrix):
        m,n=len(matrix),len(matrix[0])
        dp=[[float('inf')]*n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    dp[i][j]=0
                else:
                    if i>0:
                        dp[i][j]=min(dp[i][j],dp[i-1][j]+1)
                    if j>0:
                        dp[i][j]=min(dp[i][j],dp[i][j-1]+1)

        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if matrix[i][j]!=0:
                    if i<m-1:
                        dp[i][j]=min(dp[i][j],dp[i+1][j]+1)
                    if j<n-1:
                        dp[i][j]=min(dp[i][j],dp[i][j+1]+1)
        return dp

a=Solution()
print(a.updateMatrix([[0,0,0],
 [0,1,0],
 [1,1,1]]))



