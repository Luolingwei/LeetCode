# Input: [[1,0,0],[0,0,0],[0,0,0]]
# Output: 4
# Explanation:
# The cell (2, 2) is as far as possible from all the land with distance 4.

# 思路: 以所有岛为中心向外扩展，bfs，每次走一步，直到所有的水被覆盖，得到最大距离

class Solution:
    def maxDistance(self, grid):
        N=len(grid)
        queue=[(i,j) for i in range(N) for j in range(N) if grid[i][j]]
        dist=-1
        while queue and len(queue)!=N**2:
            new=[]
            for x,y in queue:
                for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                    i,j=x+dx,y+dy
                    if 0<=i<N and 0<=j<N and not grid[i][j]:
                        grid[i][j]=1
                        new.append((i,j))
            queue=new
            dist+=1
        return dist

a=Solution()
print(a.maxDistance([[1,0,0],[0,0,0],[0,0,0]]))
print(a.maxDistance([[1,0,1],[0,0,0],[1,0,1]]))
print(a.maxDistance([[1,1,1],[1,1,1],[1,1,1]]))