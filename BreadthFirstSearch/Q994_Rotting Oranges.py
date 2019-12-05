class Solution:
    def orangesRotting(self, grid):
        m,n=len(grid),len(grid[0])
        fresh,time=0,0
        bfs=set()
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    fresh+=1
                elif grid[i][j]==2:
                    bfs.add((i,j))
        if not fresh: return 0
        while bfs:
            new_bfs=set()
            for i,j in bfs:
                for di,dj in [(0,1),(0,-1),(-1,0),(1,0)]:
                    newi,newj=i+di,j+dj
                    if 0<=newi<m and 0<=newj<n and grid[newi][newj]==1:
                        grid[newi][newj]=2
                        new_bfs.add((newi,newj))
                        fresh-=1
            bfs=new_bfs
            time+=1
            if not fresh:
                return time
        return -1

a=Solution()
print(a.orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))
print(a.orangesRotting([[2,1,1],[0,1,1],[1,0,1]]))