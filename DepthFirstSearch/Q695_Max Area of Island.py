class Solution:
    def maxAreaOfIsland(self, grid):
        self.max=0
        def dfs(grid, i, j):
            temp=0
            if 0<=i<len(grid) and 0<=j<len(grid[0]) and grid[i][j]==1:
                grid[i][j]=0
                temp+=1
                temp+=dfs(grid,i-1,j)
                temp+=dfs(grid,i+1,j)
                temp+=dfs(grid,i,j-1)
                temp+=dfs(grid,i,j+1)
            return temp

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    self.max=max(self.max,dfs(grid,i,j))
        return self.max

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