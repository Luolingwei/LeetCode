###################### 条件设置 ########################
# 1为障碍, 0为空格子
# 输入(List[List[int]]): NxN 的矩阵 grid
# 输出(Int): 从左上角到左下角, 每个空格子正好遍历一次的路径数量

# dfs(x,y,empty) 表示 从x,y位置还剩empty个空格子没走 -> 最终状态 的方法数
# dfs(x,y,empty) = dfs(x+1,y,empty-1) + dfs(x-1,y,empty-1) + dfs(x,y+1,empty-1) + dfs(x,y-1,empty-1)

class Solution:
    def myfunction(self, grid):
        N = len(grid)
        start, end = (0,0), (N-1,0)
        # 计算空格子数量
        empty = sum([grid[i][j]==0 for i in range(N) for j in range(N)])

        def dfs(x,y,empty):
            if not (0<=x<N and 0<=y<N and grid[x][y]==0):
                return 0
            if (x,y)==end:
                return empty==1
            grid[x][y]=1
            res = dfs(x+1,y,empty-1) + dfs(x-1,y,empty-1) + dfs(x,y+1,empty-1) + dfs(x,y-1,empty-1)
            grid[x][y]=0
            return res

        return dfs(start[0],start[1],empty)


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