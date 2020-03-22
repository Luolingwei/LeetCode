
# 思路: 每一个斑块有两个可能的方向，为了保证上一块和下一块能连接起来，这里在dfs搜索的过程中判断下一块的方向中是否有当前方向的相反方向
# 若有则能连接起来， 记录visited防止回访，如果访问到 (m-1,n-1)则返回True
# 这里如果访问到已经访问过的path可直接返回False,无需backtrack
# 因为这个路口是1对1的，也就是说一旦进入某个访问过的斑块，后面的path一定是扫过的

class Solution:
    def hasValidPath(self, grid):
        m,n=len(grid),len(grid[0])
        visited=set()
        dirs={1:[(0,1),(0,-1)],
              2:[(1,0),(-1,0)],
              3:[(1,0),(0,-1)],
              4:[(1,0),(0,1)],
              5:[(0,-1),(-1,0)],
              6:[(0,1),(-1,0)]} # (0,1) 表示从上面进入, y+1 (-1,0)表示从右边进入, x-1

        def dfs(x,y):
            if (x,y)==(m-1,n-1):
                return True
            visited.add((x,y))
            for dx,dy in dirs[grid[x][y]]:
                newx,newy = x+dx,y+dy
                if 0<=newx<m and 0<=newy<n and (newx,newy) not in visited and (-dx,-dy) in dirs[grid[newx][newy]]:
                    if dfs(newx,newy): return True
            return False
        return dfs(0,0)

a=Solution()
print(a.hasValidPath([[1]]))
print(a.hasValidPath([[6,1,3],[4,1,5]]))
print(a.hasValidPath([[4,1],[6,1]]))
print(a.hasValidPath([[1,1,2]]))