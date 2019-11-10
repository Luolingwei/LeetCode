
# 思路: 先从外面(边缘)把所有0连接的地方都变成1
# 再dfs的时候所有的island都会是closed的了

class Solution:
    def closedIsland(self, grid):
        ans = 0
        m, n = len(grid), len(grid[0])
        def dfs(i, j):
            if 0 <= i < m and 0 <= j < n and not grid[i][j]:
                grid[i][j] = 1
                dfs(i + 1, j)
                dfs(i - 1, j)
                dfs(i, j + 1)
                dfs(i, j - 1)
        for i in range(m):
            dfs(i, 0)
            dfs(i, n - 1)
        for j in range(n):
            dfs(0, j)
            dfs(m - 1, j)
        for i in range(m):
            for j in range(n):
                if not grid[i][j]:
                    ans += 1
                    dfs(i, j)
        return ans

a=Solution()
print(a.closedIsland([[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]))
print(a.closedIsland([[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]))