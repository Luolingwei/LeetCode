from typing import List
class Solution:

    # dfs
    def find(self, matrix: List[List[int]]):
        m, n = len(matrix), len(matrix[0])
        def dfs(i, j):
            if i==m-1: return True
            for ni, nj in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
                if 0<=ni<m and 0<=nj<n and matrix[ni][nj]==0 and (ni,nj) not in visited:
                    visited.add((ni,nj))
                    if dfs(ni,nj):
                        return True
            return False

        for j in range(n):
            if matrix[0][j] == 0:
                visited = {(0,j)}
                if dfs(0,j):
                    return True
        return False


    # bfs
    def find2(self, matrix: List[List[int]]):
        m, n = len(matrix), len(matrix[0])
        starts = [(0,j) for j in range(n) if matrix[0][j]==0]
        bfs = set(starts)
        visited = set(starts)
        while bfs:
            new_bfs = set()
            for x,y in bfs:
                if x == m-1: return True
                for nx, ny in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
                    if 0<=nx<m and 0<=ny<n and matrix[nx][ny]==0 and (nx,ny) not in visited:
                        visited.add((nx,ny))
                        new_bfs.add((nx,ny))
            bfs = new_bfs
        return False


a=Solution()
print(a.find([[1,1,0,0],[1,0,0,1],[0,0,1,1],[0,1,0,0]]))
print(a.find2([[1,1,0,1],[1,0,0,1],[1,0,1,1],[1,0,1,1]]))