
# 思路1: dfs, 每次小球往四个方向走到尽头，然后对尽头的newx,newy dfs，每次dfs将点加入visited表示已经判断过了
# 如果碰到destination就返回True

# 思路2: bfs, 以起点为中心, 往四周寻找撞墙点, 加入new_bfs, 这里用visited记录已经遍历过的撞墙点

class Solution:

    def hasPath(self, maze, start, destination):
        m, n = len(maze), len(maze[0])
        visited=set()
        def dfs(x,y):
            if [x,y]==destination:
                return True
            visited.add((x,y))
            for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                newx,newy=x,y
                while 0<=newx+dx<m and 0<=newy+dy<n and maze[newx+dx][newy+dy]!=1:
                    newx,newy=newx+dx,newy+dy
                if (newx,newy) not in visited and dfs(newx,newy):
                    return True
            return False
        return dfs(*start)


    # def hasPath(self, maze, start, destination):
    #     m, n = len(maze), len(maze[0])
    #     bfs = [(start[0], start[1])]
    #     visited = set()
    #     while bfs:
    #         new_bfs = []
    #         for x, y in bfs:
    #             if [x, y] == destination: return True
    #             visited.add((x, y))
    #             for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
    #                 newx, newy = x, y
    #                 while 0 <= newx + dx < m and 0 <= newy + dy < n and maze[newx + dx][newy + dy] != 1:
    #                     newx, newy = newx + dx, newy + dy
    #                 if (newx, newy) not in visited:
    #                     new_bfs.append([newx, newy])
    #         bfs = new_bfs
    #     return False


a=Solution()
print(a.hasPath([[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]],[0,4],[4,4]))
print(a.hasPath([[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]],[0,4],[3,2]))