# Input: [[1, 0], [0, 1]]
# Output: 3
# Explanation: Change one 0 to 1 and connect two 1s, then we get an island with area = 3.

# 思路:
# 1.dfs每一个岛，并用index(index>1)进行标记，返回每个岛的面积并用dic记录.
# 2. 遍历整个地图，将0的点上下左右的岛屿的面积加起来.更新ans

class Solution:
    def largestIsland(self, grid):
        N=len(grid)
        def dfs(i,j,index):
            area=0
            if 0<=i<N and 0<=j<N and grid[i][j]==1:
                grid[i][j]=index
                area+=1
                area+=dfs(i+1,j,index)
                area+=dfs(i-1,j,index)
                area+=dfs(i,j+1,index)
                area+=dfs(i,j-1,index)
            return area
        dic,index,ans={},2,0
        for i in range(N):
            for j in range(N):
                if grid[i][j]==1:
                    dic[index]=dfs(i,j,index)
                    index+=1
        for i in range(N):
            for j in range(N):
                if not grid[i][j]:
                    candidate={grid[x][y] for (x,y) in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)] if 0<=x<N and 0<=y<N and grid[x][y]>1}
                    ans=max(ans,sum(dic[index] for index in candidate)+1)
        return ans or N*N

a=Solution()
print(a.largestIsland([[1, 0], [0, 1]]))
print(a.largestIsland([[1, 1], [1, 0]]))
print(a.largestIsland([[1, 1], [1, 1]]))