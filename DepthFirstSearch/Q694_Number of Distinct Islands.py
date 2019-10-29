
# 思路: 对于每个island，记录所有坐标相对起始坐标(upper left)的x,y，一样的island会有一样的坐标集合
# 可以用Set存，但是最后比较会慢，而且要转为frozenset才能用set.
# 这里可以直接将每个x,y坐标转为string存，string可以直接Hash，比较起来也更快

import collections
class Solution:
    # Solution 1 dfs+frozonset
    # def numDistinctIslands(self, grid):
    #     memo=collections.defaultdict(set)
    #     m,n=len(grid),len(grid[0])
    #     def dfs(x0,y0,x,y):
    #         if 0<=x<m and 0<=y<n and grid[x][y]:
    #             memo[(x0,y0)].add((x-x0,y-y0))
    #             grid[x][y]=0
    #             dfs(x0,y0,x+1,y)
    #             dfs(x0,y0,x-1,y)
    #             dfs(x0,y0,x,y+1)
    #             dfs(x0,y0,x,y-1)
    #     for i in range(m):
    #         for j in range(n):
    #             if grid[i][j]:
    #                 dfs(i,j,i,j)
    #     return len(set(map(frozenset,memo.values())))

    # Solution 2 dfs+string
    def numDistinctIslands(self, grid):
        memo=collections.defaultdict(frozenset)
        m,n=len(grid),len(grid[0])
        def dfs(x0,y0,x,y):
            if 0<=x<m and 0<=y<n and grid[x][y]:
                memo[(x0,y0)]+=(str(x-x0)+str(y-y0))
                grid[x][y]=0
                dfs(x0,y0,x+1,y)
                dfs(x0,y0,x-1,y)
                dfs(x0,y0,x,y+1)
                dfs(x0,y0,x,y-1)
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    dfs(i,j,i,j)
        return len(set(memo.values()))

a=Solution()
print(a.numDistinctIslands([[1,1,0,1,1],[1,0,0,0,0],[0,0,0,0,1],[1,1,0,1,1]]))