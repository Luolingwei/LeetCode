class Solution:
    def maxAreaOfIsland(self, grid):
        m,n,ans=len(grid),len(grid[0]),0
        def dfs(i, j):
            area=0
            if 0<=i<m and 0<=j<n and grid[i][j]==1:
                grid[i][j]=0
                area+=1
                area+=dfs(i-1,j)
                area+=dfs(i+1,j)
                area+=dfs(i,j-1)
                area+=dfs(i,j+1)
            return area

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    ans=max(ans,dfs(i,j))
        return ans

a=Solution()
print(a.maxAreaOfIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]))

print(a.maxAreaOfIsland([[0,0,0,0,0,0,0,0]]))
print(a.maxAreaOfIsland([[1]]))