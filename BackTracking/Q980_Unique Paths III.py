
# dfs+backtracking，与一般dfs不同的是，需要提前搜索start和end，并正好cover所有的empty

class Solution:
    def uniquePathsIII(self, grid):
        self.ans,empty=0,1
        m,n=len(grid),len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1: start=(i,j)
                if grid[i][j]==2: end=(i,j)
                if grid[i][j]==0: empty+=1

        def dfs(x,y,end,empty):
            if 0<=x<m and 0<=y<n and grid[x][y]>=0:
                if (x,y)==end:
                    self.ans+=(empty==0)
                else:
                    grid[x][y]=-1
                    dfs(x+1,y,end,empty-1)
                    dfs(x-1,y,end,empty-1)
                    dfs(x,y+1,end,empty-1)
                    dfs(x,y-1,end,empty-1)
                    grid[x][y]=0

        dfs(start[0],start[1],end,empty)
        return self.ans

a=Solution()
print(a.uniquePathsIII([[1,0,0,0],[0,0,0,0],[0,0,0,2]]))
print(a.uniquePathsIII([[1,0,0,0],[0,0,0,0],[0,0,2,-1]]))
print(a.uniquePathsIII([[0,1],[2,0]]))