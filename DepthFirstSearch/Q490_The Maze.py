
# 思路: 每次小球往四个方向走到尽头，然后对尽头的newx,newy dfs，如果某个方向不可走
# 那么newx,newy=x,y，会存在于visited中，返回Fasle，这里visited记录所有访问过的撞墙点，同样的撞墙点只需访问一次

class Solution:
    def hasPath(self, maze, start, destination):
        m, n = len(maze), len(maze[0])
        visited=set()
        def dfs(x,y):
            if (x,y) in visited:
                return False
            if [x,y]==destination:
                return True
            visited.add((x, y))
            for dx,dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                newx,newy=x,y
                while 0<=newx+dx<m and 0<=newy+dy<n and maze[newx+dx][newy+dy]!=1:
                    newx,newy=newx+dx, newy+dy
                if dfs(newx,newy):
                    return True
            return False
        return dfs(*start)

a=Solution()
print(a.hasPath([[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]],[0,4],[4,4]))
print(a.hasPath([[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]],[0,4],[3,2]))