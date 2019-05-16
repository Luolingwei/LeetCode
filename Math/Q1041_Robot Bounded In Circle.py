
# 思路: 如果执行完命令后，方向不朝原来的方向(北)，那么会回到原点，或者执行完命令后就在原点。

class Solution:
    def isRobotBounded(self, instructions):
        x,y,dx,dy=0,0,0,1
        for char in instructions:
            if char=='R':dx,dy=dy,-dx
            if char=='L':dx,dy=-dy,dx
            if char=='G':x,y=x+dx,y+dy
        return (x,y)==(0,0) or (dx,dy)!=(0,1)

a=Solution()
print(a.isRobotBounded("GGLLGG"))
print(a.isRobotBounded("GG"))
print(a.isRobotBounded("GL"))