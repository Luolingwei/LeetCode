import copy
# 按行进行dfs，高效简洁
class Solution:
    def solveNQueens(self, n):
        def dfs(i):
            if i == n: # 已添加完n行
                ans.append(path[:])
                return
            for j in range(n):
                if not any([j in cols, i + j in diag1, i - j in diag2]):
                    path.append('.'*j+'Q'+'.'*(n-j-1))
                    cols.add(j),diag1.add(i+j),diag2.add(i-j)
                    dfs(i+1)
                    # backtracking
                    cols.remove(j),diag1.remove(i+j),diag2.remove(i-j)
                    path.pop()

        ans,path=[],[]
        cols, diag1, diag2=set(),set(),set()
        dfs(0)
        return ans

a=Solution()
print(a.solveNQueens(4))