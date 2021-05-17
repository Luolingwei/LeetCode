
# 思路: 先dfs遍历所有valid的格子, 并存储每个格子的cost, 然后从(0,0)开始Dijkstra直到到达target, 返回cost

import heapq
class Solution(object):
    def findShortestPath(self, master: 'GridMaster') -> int:
        reverse_dir = {'U': 'D', 'D': 'U', 'L': 'R', 'R': 'L'}
        self.target = None
        valid = {}

        def dfs(i, j, cost):
            if master.isTarget(): self.target = (i, j)
            valid[(i, j)] = cost
            for ni, nj, dir_str in [(i + 1, j, 'D'), (i - 1, j, 'U'), (i, j + 1, 'R'), (i, j - 1, 'L')]:
                if master.canMove(dir_str) and (ni, nj) not in valid:
                    next_cost = master.move(dir_str)
                    dfs(ni, nj, next_cost)
                    master.move(reverse_dir[dir_str])

        dfs(0, 0, 0)
        q, visited = [(0, 0, 0)], {(0, 0)}
        while q:
            cur_cost, x, y = heapq.heappop(q)
            if (x, y) == self.target: return cur_cost
            for nx, ny in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if (nx, ny) not in visited and (nx, ny) in valid:
                    visited.add((nx, ny))
                    heapq.heappush(q, (cur_cost + valid[(nx, ny)], nx, ny))
        return -1
