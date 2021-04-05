class Solution:

    def find(self, matrix):

        m, n = len(matrix), len(matrix[0])
        dirs = [(1,0),(-1,0),(0,1),(0,-1),(-1,1),(1,-1),(-1,-1),(1,1)]

        def check(i,j):
            return 0 <= i < m and 0 <= j < n and matrix[i][j] == 1

        def dfs(i,j, dir):
            if not (0<=i<m and 0<=j<n): return 0
            if matrix[i][j] == 0: return 0
            else:
                return dfs(i+dir[0], j+dir[1], dir) + 1

        res = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==1:
                    for k in range(len(dirs)):
                        if not (check(i+dirs[k][0],j+dirs[k][1]) and check(i-dirs[k][0],j-dirs[k][1])):
                            res = max(res, dfs(i,j,dirs[k]))
        return res


a=Solution()
print(a.find([[0,1,1,0],[0,1,1,0],[0,0,1,0]]))
print(a.find([[1,1,0,1,1],[1,1,0,1,1],[1,1,0,1,1],[1,1,0,1,1]]))
print(a.find([[0,0,0,0,0,0,0,0,0,0],[1,1,1,1,0,0,1,1,1,1],[1,1,0,1,1,1,1,0,1,1],[1,1,0,1,1,1,1,0,1,1],[1,1,0,1,1,1,1,0,1,1],[1,1,0,1,1,1,1,0,1,1],[1,1,0,1,1,1,1,0,1,1],[1,1,0,1,1,1,1,0,1,1],[1,1,0,1,1,1,1,0,1,1],[1,1,0,1,1,1,1,0,1,1]]))