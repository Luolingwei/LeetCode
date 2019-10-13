
# 思路: bfs, 一共四种情况，往右，往下，顺时针转，逆时针转
# 这里用set作为bfs，方便查找target，每迭代一轮，判断target in bfs，O(1)时间，不需要每个进行对比. 同时，bfs用set可以去除每一轮中的重复位置

class Solution:
    def minimumMoves(self, grid):
        bfs, dist, n = {(0, 0, 0, 1)}, 0, len(grid)
        visited, target= {(0,0,0,1)},(n - 1, n - 2, n - 1, n - 1)
        # down, right, counterclock, clock
        moves = [(1, 0, 1, 0), (0, 1, 0, 1), (0, 0, -1, 1), (0, 0, 1, -1)]
        while bfs:
            new_bfs = set()
            for x1, y1, x2, y2 in bfs:
                for i, move in enumerate(moves):
                    newx1, newy1, newx2, newy2 = x1 + move[0], y1+ move[1], x2 + move[2], y2 + move[3]
                    if i<2:
                        if 0 <= newx2 < n and 0 <= newy2 < n and grid[newx1][newy1]+grid[newx2][newy2]==0 and (newx1,newy1,newx2,newy2) not in visited:
                            new_bfs.add((newx1, newy1, newx2, newy2))
                    elif i==2 and y1==y2: #确认是垂直的位置
                        if 0 <= newy2 < n and grid[newx2][newy2]+grid[x2][newy2]==0 and (newx1,newy1,newx2,newy2) not in visited:
                            new_bfs.add((newx1, newy1, newx2, newy2))
                    elif i==3 and x1==x2: #确认是水平的位置
                        if 0<= newx2 <n and grid[newx2][newy2]+grid[newx2][y2]==0 and (newx1,newy1,newx2,newy2) not in visited:
                            new_bfs.add((newx1, newy1, newx2, newy2))
            visited|=new_bfs
            bfs = new_bfs
            dist += 1
            if target in bfs: return dist
        return -1

a=Solution()
print(a.minimumMoves([[0,0,0,0,0,1],
               [1,1,0,0,1,0],
               [0,0,0,0,1,1],
               [0,0,1,0,1,0],
               [0,1,1,0,0,0],
               [0,1,1,0,0,0]]))

print(a.minimumMoves([[0,0,1,1,1,1],
               [0,0,0,0,1,1],
               [1,1,0,0,0,1],
               [1,1,1,0,0,1],
               [1,1,1,0,0,1],
               [1,1,1,0,0,0]]))

print(a.minimumMoves([[0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
                      [0,1,0,1,1,0,0,1,0,0,0,0,1,0,0],
                      [0,1,0,0,0,0,1,0,0,1,0,0,0,0,0],
                      [0,0,0,0,0,0,1,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,1,1,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0,1,0,1,0,0,0],
                      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                      [0,0,0,1,0,1,0,0,1,0,0,0,1,0,0],
                      [0,0,0,0,1,0,0,0,0,0,0,0,0,1,0],
                      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                      [0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
                      [1,0,1,1,0,0,0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
                      [1,0,0,0,0,0,1,0,0,0,1,0,0,0,1],
                      [0,0,1,0,1,0,0,0,0,0,0,0,0,0,0]]))
