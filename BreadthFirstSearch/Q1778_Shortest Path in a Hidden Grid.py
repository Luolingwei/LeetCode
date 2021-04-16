
# 思路: 由于api不能同时往四个方向bfs走, 先以起始点为(0,0) dfs搜索所有可以走到的点, 同时记录target的坐标
# 然后以(0,0)为起点bfs搜索到target的最短距离

class Solution(object):
    def findShortestPath(self, master: 'GridMaster') -> int:
        dirs = [(-1, 0, 'U'), (1, 0, 'D'), (0, -1, 'L'), (0, 1, 'R')]
        reverse_dir = {'U': 'D', 'D': 'U', 'L': 'R', 'R': 'L'}
        valid = {(0, 0)}
        self.target = None

        def dfs(i, j):
            if master.isTarget(): self.target = (i, j)
            for di, dj, dir_str in dirs:
                if (i + di, j + dj) not in valid and master.canMove(dir_str):
                    master.move(dir_str)
                    valid.add((i + di, j + dj))
                    dfs(i + di, j + dj)
                    master.move(reverse_dir[dir_str])

        dfs(0, 0)
        if not self.target: return -1
        bfs, visited, dist = {(0, 0)}, {(0, 0)}, 0
        while bfs:
            new_bfs = set()
            for x, y in bfs:
                if (x, y) == self.target: return dist
                for nx, ny in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                    if (nx, ny) in valid and (nx, ny) not in visited:
                        new_bfs.add((nx, ny))
                        visited.add((nx, ny))
            bfs = new_bfs
            dist += 1