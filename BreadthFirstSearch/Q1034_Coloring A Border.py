
# 题目意思: 点一个点，将于这个点相连的相同颜色区域的"边界"染成给定的颜色. BFS，注意不能在bfs的过程中修改grid的值，因为会对边界的判定造成影响.

class Solution:
    def colorBorder(self, grid, r0, c0, color):
        m,n=len(grid),len(grid[0])
        border,bfs,visited=set(),[(r0,c0)],{(r0,c0)}
        while bfs:
            x,y=bfs.pop(0)
            for dx,dy in [(0,1),(0,-1),(-1,0),(1,0)]:
                new_x,new_y=x+dx,y+dy
                if 0<=new_x<m and 0<=new_y<n and grid[new_x][new_y]==grid[r0][c0]:
                    if (new_x,new_y) not in visited:
                        bfs.append((new_x,new_y))
                        visited.add((new_x,new_y))
                else:
                    border.add((x,y))
        for x,y in border: grid[x][y]=color
        return grid

a=Solution()
print(a.colorBorder([[1,1],[1,2]],0,0,3))
print(a.colorBorder([[1,2,2],[2,3,2]],0,1,3))
print(a.colorBorder([[1,1,1],[1,1,1],[1,1,1]],1,1,2))
print(a.colorBorder([[1,2,1,2,1,2],[2,2,2,2,1,2],[1,2,2,2,1,2]],1,3,1))