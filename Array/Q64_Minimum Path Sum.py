class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        m = len(grid[0])
        for i in range(n):
            for j in range(m):
                # 边缘像素
                if i==0 and j!=0:
                    grid[i][j]=grid[i][j]+grid[i][j-1]
                if j==0 and i!=0:
                    grid[i][j]=grid[i][j]+grid[i-1][j]
                #非边缘像素
                if i!=0 and j!=0:
                    grid[i][j]=min(grid[i-1][j],grid[i][j-1])+grid[i][j]
        return grid[n-1][m-1]

a=Solution()
print(a.minPathSum([[1,3,1],[1,5,1],[4,2,1]]))