

class Solution:

    def find(self, matrix):
        m, n = len(matrix), len(matrix[0])
        memo = [[-1]*n for _ in range(m)]
        def dfs(x,y):
            if memo[x][y]!=-1: return memo[x][y]
            if x==m-1 and (y+1==m or matrix[x][y+1]==1) and (y-1==-1 or matrix[x][y-1]==1):
                return 0
            dist = float('-inf')
            for dx, dy in [(0,1),(0,-1),(1,0)]:
                newx, newy = x+dx, y+dy
                if 0<=newx<m and 0<=newy<n and matrix[newx][newy]==0:
                    matrix[newx][newy] = 1
                    dist = max(dist, dfs(newx,newy)+1)
                    matrix[newx][newy] = 0
            memo[x][y] = dist
            # print(dist)
            return dist

        res = -1
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    res = max(res, dfs(i,j))
        print(memo)
        return res


a=Solution()
print(a.find(
    [[1,1,0,0],
     [0,0,0,1],
     [0,0,1,1],
     [1,0,0,1]]))
