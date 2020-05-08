
# dfs+backtracking，与一般dfs不同的是，需要提前搜索start和end，并正好cover所有的empty

class Solution:
    # solution 1 dfs
    # def uniquePathsIII(self, grid):
    #     self.ans,empty=0,1
    #     m,n=len(grid),len(grid[0])
    #     for i in range(m):
    #         for j in range(n):
    #             if grid[i][j]==1: start=(i,j)
    #             if grid[i][j]==2: end=(i,j)
    #             if grid[i][j]==0: empty+=1
    #
    #     def dfs(x,y,end,empty):
    #         if 0<=x<m and 0<=y<n and grid[x][y]>=0:
    #             if (x,y)==end:
    #                 self.ans+=(empty==0)
    #             else:
    #                 grid[x][y]=-1
    #                 dfs(x+1,y,end,empty-1)
    #                 dfs(x-1,y,end,empty-1)
    #                 dfs(x,y+1,end,empty-1)
    #                 dfs(x,y-1,end,empty-1)
    #                 grid[x][y]=0
    #
    #     dfs(start[0],start[1],end,empty)
    #     return self.ans

    # Solution 2 dfs + memo, using bit mask to memorize
    def uniquePathsIII(self, grid):
        final = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == -1: continue
                if grid[i][j] == 1:
                    start = (i, j)
                if grid[i][j] == 2:
                    end = (i, j)
                final |= (1 << (i * n + j))

        memo = {}

        def dfs(x, y, visited):
            if not (0 <= x < m and 0 <= y < n and grid[x][y] >= 0):
                return 0
            new_visited = visited | (1 << (x * n + y))
            if (x, y) == end:
                return new_visited == final
            if (x, y, visited) in memo:
                return memo[(x, y, visited)]
            grid[x][y] = -1
            res = dfs(x + 1, y, new_visited) + dfs(x - 1, y, new_visited) + dfs(x, y + 1, new_visited) + dfs(x, y - 1,new_visited)
            grid[x][y] = 0
            memo[(x, y, visited)] = res
            return res

        return dfs(start[0], start[1], 0)

a=Solution()
print(a.uniquePathsIII([[1,0,0,0],[0,0,0,0],[0,0,0,2]]))
print(a.uniquePathsIII([[1,0,0,0],[0,0,0,0],[0,0,2,-1]]))
print(a.uniquePathsIII([[0,1],[2,0]]))