
# 找出所有可能的起点，分别做dfs，求所有路径中的最大sumG，路径结束时再更新self.maxG

class Solution:
    def getMaximumGold(self, grid):
        m, n = len(grid), len(grid[0])
        starts = [(i, j) for i in range(m) for j in range(n) if grid[i][j]]
        self.maxG = 0

        def dfs(i, j, curG, visited):
            if 0 <= i < m and 0 <= j < n and grid[i][j] and (i, j) not in visited:
                curG += grid[i][j]
                visited.add((i, j))
                dfs(i + 1, j, curG, visited)
                dfs(i - 1, j, curG, visited)
                dfs(i, j + 1, curG, visited)
                dfs(i, j - 1, curG, visited)
                visited.remove((i, j))
            else:
                self.maxG = max(self.maxG, curG)

        for x, y in starts:
            dfs(x, y, 0, set())
        return self.maxG