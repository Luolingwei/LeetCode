
# 思路1: 从所有的empty进行bfs搜索，直到达到所有的building或者的bfs搜索结束，记录总距离
# 思路2: 从所有的building进行bfs搜索，对每个empty记录各building到达该点的最短距离，能收集所有building距离的点为合格点

import collections
class Solution:

    # 思路1 TLE
    # def shortestDistance(self, grid):
    #     m, n = len(grid), len(grid[0])
    #     empty, ans = [], float('inf')
    #     building = 0
    #     for i in range(m):
    #         for j in range(n):
    #             if grid[i][j] == 1:
    #                 building += 1
    #             elif grid[i][j] == 0:
    #                 empty.append((i, j))
    #
    #     def bfs(i, j):
    #         res = 0
    #         q = collections.deque([(i, j, 0)])
    #         visited = {(i, j)}
    #         left = building
    #         while left and q:
    #             x, y, dist = q.popleft()
    #             for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
    #                 newx, newy = x + dx, y + dy
    #                 if 0 <= newx < m and 0 <= newy < n and (newx, newy) not in visited:
    #                     if grid[newx][newy] == 0:
    #                         q.append((newx, newy, dist + 1))
    #                     elif grid[newx][newy] == 1:
    #                         res += (dist + 1)
    #                         left -= 1
    #                     visited.add((newx, newy))
    #         return res if not left else float('inf')
    #
    #     for i, j in empty:
    #         ans = min(ans, bfs(i, j))
    #     return ans if ans != float('inf') else -1


    # 思路2 660 ms
    def shortestDistance(self, grid):
        m, n = len(grid), len(grid[0])
        memo = [[[] for _ in range(n)] for _ in range(m)]
        building, ans = 0, float('inf')

        def bfs(i, j):
            q = collections.deque([(i, j, 0)])
            visited = [[0] * n for _ in range(m)]
            visited[i][j] = 1
            while q:
                x, y, dist = q.popleft()
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    newx, newy = x + dx, y + dy
                    if 0 <= newx < m and 0 <= newy < n and not visited[newx][newy]:
                        if grid[newx][newy] == 0:
                            q.append((newx, newy, dist + 1))
                            memo[newx][newy].append(dist + 1)
                        visited[newx][newy] = 1

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    bfs(i, j)
                    building += 1

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    if len(memo[i][j]) == building:
                        ans = min(ans, sum(memo[i][j]))
        return ans if ans != float('inf') else -1

a=Solution()
print(a.shortestDistance([[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]))