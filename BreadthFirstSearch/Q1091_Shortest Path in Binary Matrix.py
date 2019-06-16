
# 思路: bfs标准解法，注意用visited避免回访

class Solution:
    def shortestPathBinaryMatrix(self, grid):
        m,n=len(grid),len(grid[0])
        if grid[0][0] or grid[m-1][n-1]: return -1
        queue,visited=[(1,0,0)],{(0,0)}
        while queue:
            dist,x,y=queue.pop(0)
            if x==m-1 and y==n-1: return dist
            for dx,dy in [(0,1),(0,-1),(-1,0),(1,0),(1,1),(-1,-1),(-1,1),(1,-1)]:
                new_x,new_y=x+dx,y+dy
                if 0<=new_x<m and 0<=new_y<n and (new_x,new_y) not in visited and grid[new_x][new_y]==0:
                    queue.append((dist+1,new_x,new_y))
                    visited.add((new_x,new_y))
        return -1

a=Solution()
print(a.shortestPathBinaryMatrix([[0,1],[1,0]]))
print(a.shortestPathBinaryMatrix([[0,0,0],[1,1,0],[1,1,0]]))
print(a.shortestPathBinaryMatrix([[0,0,0],[1,1,0]]))
print(a.shortestPathBinaryMatrix([[0,0,0,0,1],[1,0,0,0,0],[0,1,0,1,0],[0,0,0,1,1],[0,0,0,1,0]]))