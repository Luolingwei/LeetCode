###################### 条件设置 ########################
# 1为障碍, 0为空格子
# 输入(List[List[int]]): NxN 的矩阵 grid
# 输出(Int): 从左上角到左下角, 每个空格子正好遍历一次的路径数量

# dfs(x,y,visited) 表示 当前位置x,y, 已经走过的path为visited -> 最终状态 的方法数
# dfs(x,y,visited) = dfs(x+1,y,new_visited) + dfs(x-1,y,new_visited) + dfs(x,y+1,new_visited) + dfs(x,y-1,new_visited)
from functools import lru_cache

class Solution:
    def myfunction(self, grid):
        N = len(grid)
        final = 0
        start, end = (0,0), (N-1,0)
        # 将所有空格子的(x,y)用位运算存储
        for i in range(N):
            for j in range(N):
                if grid[i][j] == 0:
                    final |= 1<<(i*N)+j

        # 不要形成孤立的区域。如果行走过程中把路一分为二，那么肯定有一部分再也走不到了，需要剪枝。
        def helper1(x,y):
            up,down,left,right=0,0,0,0
            if x-1<0 or grid[x-1][y]==1:
                up = 1
            if x+1>=N or grid[x+1][y]==1:
                down = 1
            if y-1<0 or grid[x][y-1]==1:
                left = 1
            if y+1>=N or grid[x][y+1]==1:
                right = 1
            # 当前点左右都是已经点(包括边缘)，而上下都是未经点；
            # 当前点上下都是已经点(包括边缘)，而左右都是未经点。
            if left and right and not up and not down:
                return False
            if not left and not right and up and down:
                return False
            return True

        # 判断(x,y)四周有几个未经点
        def helper2(x,y):
            res = 0
            if 0<=x<N and 0<=y<N and grid[x][y]==0:
                for newx,newy in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
                    if 0<=newx<N and 0<=newy<N and grid[newx][newy]==0:
                        res += 1
            return res

        memo = {}
        @lru_cache(None)
        def dfs(x,y,visited):
            if not (0<=x<N and 0<=y<N and grid[x][y]==0):
                return 0
            new_visited = visited|(1<<(x*N)+y)
            if (x,y)==end:
                return new_visited==final
            if not helper1(x,y):
                memo[(x,y,visited)] = 0
                return 0
            if (x,y,visited) in memo:
                return memo[(x,y,visited)]
            # 统计周围必经点个数
            count = 0
            for newx,newy in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
                notvisited = helper2(newx,newy)
                # 只有一个相邻的未经点, 这个成为必经点
                if notvisited == 1:
                    tx,ty = newx, newy
                    count+=1
            # 大于1个必经点
            if count>1:
                memo[(x, y, visited)] = 0
                return 0
            # 只有1个必经点, 走这个
            if count == 1:
                grid[x][y] = 1
                memo[(x, y, visited)] = dfs(tx,ty,new_visited)
                grid[x][y] = 0
                return memo[(x, y, visited)]
            # 没有必经点
            grid[x][y] = 1
            res = dfs(x+1,y,new_visited) + dfs(x-1,y,new_visited) + dfs(x,y+1,new_visited) + dfs(x,y-1,new_visited)
            grid[x][y]=0
            memo[(x,y,visited)] = res
            return res

        return dfs(start[0],start[1],0)


a=Solution()
print(a.myfunction([[0,0],[0,0]]))
print(a.myfunction([[1,0],[0,0]]))
print(a.myfunction([[0,1],[0,0]]))
print(a.myfunction([[0,0],[1,0]]))
print(a.myfunction([[0,0],[0,1]]))
print(a.myfunction([[0,0,0],[0,0,0],[0,0,0]]))
print(a.myfunction([[0,1,0],[0,0,0],[0,0,0]]))
print(a.myfunction([[0,0,0],[0,1,0],[0,0,0]]))
print(a.myfunction([[0,0,0],[0,0,0],[0,1,0]]))
print(a.myfunction([[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]))
print(a.myfunction([[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]))
print(a.myfunction([[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]))