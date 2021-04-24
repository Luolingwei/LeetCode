class Solution:

    def find(self, matrix):
        m, n = len(matrix), len(matrix[0])

        def mark_border(i,j):
            if 0<=i<m and 0<=j<n and matrix[i][j] == 0:
                matrix[i][j] = -1
                mark_border(i+1,j)
                mark_border(i-1,j)
                mark_border(i,j+1)
                mark_border(i,j-1)

        def dfs(i,j):
            area = 0
            if 0<=i<m and 0<=j<n and matrix[i][j] != -1:
                area += 1
                matrix[i][j] = -1
                area += dfs(i+1,j)
                area += dfs(i-1,j)
                area += dfs(i,j+1)
                area += dfs(i,j-1)
            return area

        for i in range(m):
            if matrix[i][0] == 0: mark_border(i,0)
            if matrix[i][n-1] == 0: mark_border(i, n-1)
        for j in range(n):
            if matrix[0][j] == 0: mark_border(0,j)
            if matrix[m-1][j] == 0: mark_border(m-1,j)
        res = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j]!=-1:
                    res = max(res, dfs(i,j))
        return res


    def find2(self, matrix):
        m, n = len(matrix), len(matrix[0])

        def mark_border(i,j):
            if 0<=i<m and 0<=j<n and matrix[i][j] == 0:
                matrix[i][j] = -2
                mark_border(i+1,j)
                mark_border(i-1,j)
                mark_border(i,j+1)
                mark_border(i,j-1)

        def dfs(i,j):
            if 0<=i<m and 0<=j<n and matrix[i][j] == 0:
                inner_lake.add((i,j))
                matrix[i][j] = -1
                dfs(i+1,j)
                dfs(i-1,j)
                dfs(i,j+1)
                dfs(i,j-1)

        def bfs(inner_lake: set):
            dist = 0
            while inner_lake:
                new_inner_lake = set()
                for x,y in inner_lake:
                    matrix[x][y] = -1
                    for nx,ny in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
                        if not (0<=nx<m and 0<=ny<n) or matrix[nx][ny] == -2:
                            return dist
                        elif matrix[nx][ny]==1:
                            new_inner_lake.add((nx,ny))
                inner_lake = new_inner_lake
                dist+=1

        for i in range(m):
            if matrix[i][0] == 0: mark_border(i, 0)
            if matrix[i][n - 1] == 0: mark_border(i, n - 1)
        for j in range(n):
            if matrix[0][j] == 0: mark_border(0, j)
            if matrix[m - 1][j] == 0: mark_border(m - 1, j)

        inner_lake = set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    dfs(i,j)

        return bfs(inner_lake)


a=Solution()
print(a.find([[1,1,1,1,1],
              [1,1,0,1,1],
              [0,0,1,0,0],
              [1,0,1,1,1],
              [1,1,1,0,1]]))

print(a.find2([[1,1,1,1,1],
               [1,0,1,1,1],
               [1,1,0,1,1],
               [1,1,1,1,1],
               [1,1,1,1,0]]))
