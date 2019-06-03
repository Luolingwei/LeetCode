class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m,n=len(obstacleGrid),len(obstacleGrid[0])
        dp=[[0]*(n+1) for _ in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if i+j==2:
                    dp[i][j]=1-obstacleGrid[i-1][j-1]
                else:
                    if obstacleGrid[i-1][j-1]:
                        dp[i][j]=0
                    else:
                        dp[i][j]=dp[i-1][j]+dp[i][j-1]
        return dp[-1][-1]

a=Solution()
print(a.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))
print(a.uniquePathsWithObstacles([[0,0],[1,1],[0,0]]))
print(a.uniquePathsWithObstacles([[0,0],[1,0]]))
print(a.uniquePathsWithObstacles([[0,1]]))
print(a.uniquePathsWithObstacles([[0,0,0]]))
print(a.uniquePathsWithObstacles([[0],[0],[1]]))
print(a.uniquePathsWithObstacles([[1,0],[0,0],[0,0]]))
