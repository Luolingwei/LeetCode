class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        n=len(obstacleGrid)
        m=len(obstacleGrid[0])
        if obstacleGrid[0][0]==1:#左上角像素为障碍
            return 0
        for i in range(n):
            for j in range(m):
                # 边缘像素
                if i==0 or j==0:
                    if obstacleGrid[i][j]==0: #无障碍
                        if i==0 and j==0:
                            obstacleGrid[i][j]=1
                        if i==0 and j!=0:
                            obstacleGrid[i][j]=obstacleGrid[i][j-1]
                        if j==0 and i!=0:
                            obstacleGrid[i][j] = obstacleGrid[i-1][j]
                    else: #有障碍
                        obstacleGrid[i][j]=0
                 # 非边缘像素
                elif obstacleGrid[i][j]==0: #无障碍
                    obstacleGrid[i][j]=obstacleGrid[i-1][j]+obstacleGrid[i][j-1]
                else: #有障碍
                    obstacleGrid[i][j]=0
        return obstacleGrid[n-1][m-1]

a=Solution()
print(a.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))
print(a.uniquePathsWithObstacles([[0,0],[1,1],[0,0]]))
print(a.uniquePathsWithObstacles([[0,0],[1,0]]))
print(a.uniquePathsWithObstacles([[0,1]]))
print(a.uniquePathsWithObstacles([[0,0,0]]))
print(a.uniquePathsWithObstacles([[0],[0],[1]]))
