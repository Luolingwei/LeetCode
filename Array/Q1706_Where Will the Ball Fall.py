
# 思路: 模拟每个小球的掉落过程
# 如果当前是1那么比较和右边的是否一致，如果是-1比较和左边的是否一致
# 如果一致则可以下落，否则返回-1

class Solution:
    def findBall(self, grid):
        m,n = len(grid), len(grid[0])
        res = [-1]*n
        for i in range(n):
            y, x = 0, i
            while y<m:
                delta = grid[y][x]
                if not 0<=x+delta<n: break
                if grid[y][x]==grid[y][x+delta]:
                    x += grid[y][x]
                    y += 1
                else:
                    break
            if y==m: res[i] = x
        return res

a=Solution()
print(a.findBall([[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]))
print(a.findBall([[1]]))
print(a.findBall([[-1]]))