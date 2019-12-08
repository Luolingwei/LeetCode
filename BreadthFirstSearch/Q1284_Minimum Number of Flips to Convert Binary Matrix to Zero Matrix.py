import collections
from copy import deepcopy

# bfs每次变一个格子

class Solution:
    def minFlips(self, mat):
        m, n = len(mat), len(mat[0])
        def flip(curmat, x, y, curs):
            mat = deepcopy(curmat)
            for dx, dy in [(0, 0), (0, 1), (0, -1), (1, 0), (-1, 0)]:
                newx, newy = x + dx, y + dy
                if 0 <= newx < m and 0 <= newy < n:
                    old = mat[newx][newy]
                    mat[newx][newy] = 1 - old
                    curs = curs + 1 - 2 * old
            return mat, curs

        visited = {str(mat)}
        bfs = collections.deque()
        bfs.append((0, mat, sum(map(sum, mat))))
        while bfs:
            curdist, curmat, curs = bfs.popleft()
            if curs == 0:
                return curdist
            for i in range(m):
                for j in range(n):
                    nextmat, nexts = flip(curmat, i, j, curs)
                    if str(nextmat) not in visited:
                        bfs.append((curdist + 1, nextmat, nexts))
                        visited.add(str(nextmat))
        return -1

a=Solution()
print(a.minFlips([[0,0],[0,1]]))
print(a.minFlips([[0]]))
print(a.minFlips([[1,1,1],[1,0,1],[0,0,0]]))
print(a.minFlips([[1,0,0],[1,0,0]]))