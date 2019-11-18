
# 思路: bfs每次走一格，visited记录(箱子来的坐标，箱子到的坐标)
# 每次能走的条件是 1.推到的地方不是'#' 2.人推的地方不是'#' 3.人能从上次箱子的位置到现在要推的地方 4.(箱子来的坐标,箱子到的坐标)不重复
# find每次把箱子的位置当成'#'，判断人是否能从上次停的地方到推的地方，每次都要find是因为箱子在移动，墙的情况会改变

import collections
class Solution:
    def minPushBox(self, grid):
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 'S':
                    P = (i, j)
                if grid[i][j] == 'B':
                    B = (i, j)
                if grid[i][j] == 'T':
                    T = (i, j)

        def find(i, j, ti, tj, boxi, boxj):
            if 0 <= i < m and 0 <= j < n and grid[i][j] != '#' and (i, j) != (boxi, boxj) and (i, j) not in memo:
                memo.add((i, j))
                if (i, j) == (ti, tj):
                    return True
                if find(i + 1, j, ti, tj, boxi, boxj) \
                    or find(i - 1, j, ti, tj, boxi, boxj) \
                    or find(i, j + 1, ti, tj,boxi, boxj) \
                    or find(i, j - 1, ti, tj, boxi, boxj):
                    return True
            return False

        bfs = collections.deque()
        bfs.append((P[0], P[1], B[0], B[1], 0))
        visited = {(P[0], P[1], B[0], B[1])}
        while bfs:
            prex, prey, curx, cury, curd = bfs.popleft()
            if (curx, cury) == T: return curd
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                tox, toy = curx + dx, cury + dy
                fromx, fromy = curx - dx, cury - dy
                memo = set()
                if 0 <= tox < m and 0 <= toy < n and grid[tox][toy] != '#' \
                        and 0 <= fromx < m and 0 <= fromy < n and grid[fromx][fromy] != '#' \
                        and find(prex, prey, fromx, fromy, curx, cury) and (curx, cury, tox, toy) not in visited:
                    visited.add((curx, cury, tox, toy))
                    bfs.append((curx, cury, tox, toy, curd + 1))
        return -1

a=Solution()
print(a.minPushBox([["#","#","#","#","#","#"],
                    ["#","T","#","#","#","#"],
                    ["#",".",".","B",".","#"],
                    ["#",".","#","#",".","#"],
                    ["#",".",".",".","S","#"],
                    ["#","#","#","#","#","#"]]))

print(a.minPushBox([["#",".",".","#","T","#","#","#","#"],
                    ["#",".",".","#",".","#",".",".","#"],
                    ["#",".",".","#",".","#","B",".","#"],
                    ["#",".",".",".",".",".",".",".","#"],
                    ["#",".",".",".",".","#",".","S","#"],
                    ["#",".",".","#",".","#","#","#","#"]]))

print(a.minPushBox([["#",".",".","#","#","#","#","#"],
                    ["#",".",".","T","#",".",".","#"],
                    ["#",".",".",".","#","B",".","#"],
                    ["#",".",".",".",".",".",".","#"],
                    ["#",".",".",".","#",".","S","#"],
                    ["#",".",".","#","#","#","#","#"]]))

print(a.minPushBox([["#","#","#","#","#","#","#"],
                    ["#","S","#",".","B","T","#"],
                    ["#","#","#","#","#","#","#"]]))