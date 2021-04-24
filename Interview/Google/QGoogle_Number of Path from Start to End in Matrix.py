
class Solution:
    def find(self, matrix, start, end):
        m, n = len(matrix), len(matrix[0])
        self.res = 0
        def dfs(i,j):
            if 0<=i<m and 0<=j<n and matrix[i][j]==0:
                if [i, j] == end: self.res += 1
                matrix[i][j] = 1
                dfs(i+1, j)
                dfs(i-1, j)
                dfs(i, j+1)
                dfs(i, j-1)
                matrix[i][j] = 0

        dfs(start[0],start[1])
        return self.res


    def find2(self, matrix, start, end):
        m, n = len(matrix), len(matrix[0])
        def dfs(i,j):
            if [i, j] == end: return 1
            res = 0
            if 0<=i<m and 0<=j<n and matrix[i][j]==0:
                matrix[i][j] = 1
                res += dfs(i+1, j)
                res += dfs(i-1, j)
                res += dfs(i, j+1)
                res += dfs(i, j-1)
                matrix[i][j] = 0
            return res
        return dfs(start[0],start[1])


a=Solution()
print(a.find([[0,0,0],
              [1,0,0],
              [1,0,0]],[0,0], [2,2]))

print(a.find2([[0,0,0],
              [1,0,0],
              [1,0,0]],[0,0], [2,2]))