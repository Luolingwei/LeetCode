import heapq

# 思路: 用Dijskra方法, 每次从heap中pop出dist最小的stop点, pop到终点时返回dist

class Solution:
    def shortestDistance(self, maze, start, destination):
        m,n=len(maze),len(maze[0])
        q = [(0,start[0],start[1])]
        visited = set()
        while q:
            dist,x,y = heapq.heappop(q)
            if [x,y]==destination: return dist
            visited.add((x,y))
            for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                newx,newy,plus=x,y,0
                while 0<=newx+dx<m and 0<=newy+dy<n and maze[newx+dx][newy+dy]!=1:
                    newx,newy=newx+dx,newy+dy
                    plus+=1
                if (newx,newy) not in visited:
                    heapq.heappush(q,(dist+plus,newx,newy))
        return -1

a=Solution()
print(a.shortestDistance([[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]],[0,4],[4,4]))