
# 全局变量调用：想要在自定义的函数中使用全局变量，要在函数中使用global的声明
# 嵌套函数中的变量的调用：要在嵌套的变量中使用外部变量，则要使用nonlocal的声明
# list,set,tuple等不受限制

class Solution:
    def totalNQueens(self, n):
        def dfs(i):
            nonlocal count
            if i==n:
                count+=1
            for j in range(n):
                if not any([j in cols,i+j in diag1,i-j in diag2]):
                    cols.add(j),diag1.add(i+j),diag2.add(i-j)
                    dfs(i+1)
                    cols.remove(j),diag1.remove(i+j),diag2.remove(i-j)
        count=0
        cols,diag1,diag2=set(),set(),set()
        dfs(0)
        return count

a=Solution()
print(a.totalNQueens(4))
