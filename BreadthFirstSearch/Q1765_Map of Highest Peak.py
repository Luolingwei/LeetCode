
# 思路: 从water的点开始向外Bfs, 每次dist+1, 直到遍历完所有的点

class Solution:
    def highestPeak(self, isWater):
        m, n, dist = len(isWater), len(isWater[0]), 1
        q = []
        for i in range(m):
            for j in range(n):
                if isWater[i][j]:
                    q.append((i,j))
                    isWater[i][j] = 0
        waters = set(q)
        while q:
            newq = []
            for x,y in q:
                for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                    newx, newy = x + dx, y + dy
                    if 0<=newx<m and 0<=newy<n and isWater[newx][newy] == 0 and (newx,newy) not in waters:
                        isWater[newx][newy] = dist
                        newq.append((newx,newy))
            dist+=1
            q = newq
        return isWater


a=Solution()
print(a.highestPeak([[0,1],[0,0]]))
print(a.highestPeak([[0,0,1],[1,0,0],[0,0,0]]))