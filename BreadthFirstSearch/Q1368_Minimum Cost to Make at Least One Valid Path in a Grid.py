
# 思路: 每次以当前点dfs扩展所有能直接到达的点, 并直接记录最短dist
# 以上一轮增加的点的为起始点集, 改变4个方向继续扩展, 得到新的点集, 此轮dist+1
# memo[i][j]表示(0,0)到该点需要改变几次方向

class Solution:
    def minCost(self, grid):
        dist = 0
        m, n = len(grid), len(grid[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        memo = [[-1] * n for _ in range(m)]
        q, preq = [], []

        def dfs(i, j):
            if not (0 <= i < m and 0 <= j < n and memo[i][j] == -1): return
            memo[i][j] = dist
            q.append((i, j))
            dfs(i + dirs[grid[i][j] - 1][0], j + dirs[grid[i][j] - 1][1])

        dfs(0, 0)
        while q:
            dist += 1
            preq, q = q, []
            for x, y in preq:
                for dx, dy in dirs:
                    dfs(x + dx, y + dy)
        return memo[-1][-1]


a=Solution()
print(a.minCost([[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]]))
print(a.minCost([[1,1,3],[3,2,2],[1,1,4]]))
print(a.minCost([[1,2],[4,3]]))
print(a.minCost([[2,2,2],[2,2,2]]))
print(a.minCost([[4]]))