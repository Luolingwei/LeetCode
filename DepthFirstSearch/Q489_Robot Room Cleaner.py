
# 思路: 对room进行dfs搜索，用visited记录已经访问过的坐标，在每个点进行上下左右dfs
# backtracking时
# turnRight(),turnRight(),move(),turnRight(),turnRight()表示后退一步
# turnRight()表示向右旋转一步，正好方向也取到下一个
# 这样来匹配dfs和robot的移动

class Solution:
    def cleanRoom(self, robot):
        moves=[(0,-1),(1,0),(0,1),(-1,0)] # up right down left
        visited = set()
        def dfs(x,y,dirs):
            robot.clean()
            visited.add((x,y))
            for i in range(4):
                dx,dy=moves[(dirs+i)%4]
                if (x+dx,y+dy) not in visited and robot.move():
                    dfs(x+dx,y+dy,(dirs+i)%4)
                    robot.turnRight()
                    robot.turnRight()
                    robot.move()
                    robot.turnRight()
                    robot.turnRight()
                robot.turnRight()
        dfs(0,0,0)