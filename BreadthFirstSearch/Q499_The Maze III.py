import heapq

# 思路: hole可能在路途中间而不是stop的点, 所以在向新方向移动时要同时判断是否到达了hole
# 如果到达了, 将当前点加入heap, 等到它成为最小dist时, 会被pop
# heap以(dist,pattern,x,y)存储, 首先取最短路径, 如果长度一样取pattern小的

class Solution:
    def findShortestWay(self, maze, ball, hole) -> str:
        m,n=len(maze),len(maze[0])
        q = [(0,"",ball[0],ball[1])]
        visited = set()
        while q:
            dist,pattern,x,y = heapq.heappop(q)
            if [x,y]==hole: return pattern
            visited.add((x,y))
            for dx,dy,c in ([(0,1,"r"),(0,-1,"l"),(1,0,"d"),(-1,0,"u")]):
                newx,newy,plus=x,y,0
                while 0<=newx+dx<m and 0<=newy+dy<n and maze[newx+dx][newy+dy]!=1:
                    newx,newy=newx+dx,newy+dy
                    plus+=1
                    if [newx,newy]==hole:
                        break
                if (newx,newy) not in visited:
                    heapq.heappush(q,(dist+plus,pattern+c,newx,newy))
        return "impossible"


a=Solution()
print(a.findShortestWay([[0,0,0,0,0],[1,1,0,0,1],[0,0,0,0,0],[0,1,0,0,1],[0,1,0,0,0]],[4,3],[0,1]))
print(a.findShortestWay([[0,0,0,0,0],[1,1,0,0,1],[0,0,0,0,0],[0,1,0,0,1],[0,1,0,0,0]],[4,3],[3,0]))