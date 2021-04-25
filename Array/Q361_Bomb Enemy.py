
# 思路: 记录当前row和当前col后面可以kill的enemy个数, 如果没有碰到墙就不需要重新计算,
# 如果碰到墙重新遍历后面的计算row_kill, col_kill
# 因为先遍历行后列, 只需记录一个row_kill, n个col_kill

class Solution:
    def maxKilledEnemies(self, grid):
        m, n = len(grid), len(grid[0])
        row_res, col_res = 0, [0] * n

        def row_kill(i, j):
            res = 0
            while j < n and grid[i][j] != 'W':
                res += grid[i][j] == 'E'
                j += 1
            return res

        def col_kill(i, j):
            res = 0
            while i < m and grid[i][j] != 'W':
                res += grid[i][j] == 'E'
                i += 1
            return res

        ans = 0
        for i in range(m):
            for j in range(n):
                if j == 0 or grid[i][j - 1] == 'W':
                    row_res = row_kill(i, j)
                if i == 0 or grid[i - 1][j] == 'W':
                    col_res[j] = col_kill(i, j)
                if grid[i][j] == '0':
                    ans = max(ans, row_res + col_res[j])
        return ans

a=Solution()
print(a.maxKilledEnemies([["0","E","0","0"],["E","0","W","E"],["0","E","0","0"]]))
print(a.maxKilledEnemies([["W","W","W"],["0","0","0"],["E","E","E"]]))