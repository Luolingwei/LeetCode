
# 思路1: uf, 用每个点的绝对坐标(一维)用在uf中, 将所有点从大到小排序, 每次点亮一个点, 并与其四周相连(如果四周点亮),
# 一旦(0,0)和(m-1,n-1)相通, 则返回此时的v, 为路径的最小值
# O(mnlogmn)

# 思路2: dijkstra, 每次pop出当前路径最小值最大的点, 更新最小值, 直到第一个点到达(m-1,n-1), O(mnlogmn)

import heapq

class Solution:
    def maximumMinimumPath(self, A):
        m, n = len(A), len(A[0])
        points = sorted([(-A[i][j], i, j) for i in range(m) for j in range(n)])
        visited = [[0] * n for _ in range(m)]
        uf = [i * n + j for i in range(m) for j in range(n)]

        def find(x):
            if uf[x] != x:
                uf[x] = find(uf[x])
            return uf[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px == py: return False
            uf[px] = py
            return True

        for v, i, j in points:
            visited[i][j] = 1
            for ni, nj in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= ni < m and 0 <= nj < n and visited[ni][nj]:
                    union(i * n + j, ni * n + nj)
            if find(0) == find((m - 1) * n + n-1):
                return -v

        return -1


    def maximumMinimumPath2(self, A):
        m, n = len(A), len(A[0])
        q = [(-A[0][0], 0, 0)]
        visited = [[0]*n for _ in range(m)]
        visited[0][0] = 1
        while q:
            v, x, y = heapq.heappop(q)
            if (x,y) == (m-1,n-1): return -v
            for nx,ny in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
                if 0<=nx<m and 0<=ny<n and not visited[nx][ny]:
                    visited[nx][ny] = 1
                    heapq.heappush(q,(-min(-v,A[nx][ny]), nx, ny))
        return -1


a=Solution()
print(a.maximumMinimumPath([[5,4,5],[1,2,6],[7,4,6]]))
print(a.maximumMinimumPath([[2,2,1,2,2,2],[1,2,2,2,1,2]]))
print(a.maximumMinimumPath([[3,4,6,3,4],[0,2,1,1,7],[8,8,3,2,7],[3,2,4,9,8],[4,1,2,0,0],[4,6,5,4,3]]))
print(a.maximumMinimumPath2([[5,4,5],[1,2,6],[7,4,6]]))
print(a.maximumMinimumPath2([[2,2,1,2,2,2],[1,2,2,2,1,2]]))
print(a.maximumMinimumPath2([[3,4,6,3,4],[0,2,1,1,7],[8,8,3,2,7],[3,2,4,9,8],[4,1,2,0,0],[4,6,5,4,3]]))