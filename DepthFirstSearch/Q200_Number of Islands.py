class Solution:
    def dfs(self,grid,i,j):
        if -1<i<len(grid) and -1<j<len(grid[0]) and grid[i][j]=='1':
            grid[i][j]='0'
        else: return
        self.dfs(grid,i,j-1)
        self.dfs(grid,i,j+1)
        self.dfs(grid,i+1,j)
        self.dfs(grid,i-1,j)

    def numIslands(self, grid):
        island=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='1':
                    self.dfs(grid,i,j)
                    island+=1
        return island

a=Solution()
print(a.numIslands([['1','1','1','1','0'],['1','1','0','1','0'],['1','1','0','0','0'],['0','0','0','0','0']]))
print(a.numIslands([['1','0','0','0','0'],['0','1','0','0','0'],['0','0','1','0','0'],['0','0','0','1','0']]))
print(a.numIslands([['1','1','0','0','0'],['1','1','0','0','0'],['0','0','1','0','0'],['0','0','0','1','1']]))
print(a.numIslands([['1','1','0','0','0']]))
print(a.numIslands([[]]))