
# 思路: bfs，先求出其中一个岛的所有坐标，然后从找出的岛出发,bfs，寻找另外一个岛.
# 将已经遍历过的元素标记为-1，避免重复访问，也可以使非岛边缘像素在bfs的第一轮就出局.

class Solution:
    def shortestBridge(self, A):
        def dfs(i,j):
            if 0<=i<n and 0<=j<n and A[i][j]==1:
                first.append((i,j,0))
                A[i][j]=-1
                dfs(i+1,j),dfs(i-1,j),dfs(i,j+1),dfs(i,j-1)
        def get_island():
            for i in range(n):
                for j in range(n):
                    if A[i][j] == 1: return i, j
        first,dist,n=[],0,len(A)
        dfs(*get_island())
        while first:
            x,y,dist=first.pop(0)
            for dx,dy in [(0,1),(1,0),(0,-1),(-1,0)]:
                new_x,new_y=x+dx,y+dy
                if 0<=new_x<n and 0<=new_y<n:
                    if A[new_x][new_y]==1:
                        return dist
                    if A[new_x][new_y]==0:
                        first.append((new_x,new_y,dist+1))
                        A[new_x][new_y]=-1

a=Solution()
print(a.shortestBridge([[0,1],[1,0]]))
print(a.shortestBridge([[1,1,1],[0,1,0],[0,0,1]]))
print(a.shortestBridge([[0,1,0],[0,0,0],[0,0,1]]))
print(a.shortestBridge([[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]))