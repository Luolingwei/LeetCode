
# 思路: check 8个方向，如果遇到Q或者出界break，如果有Q加入ans,

class Solution:
    def queensAttacktheKing(self, queens, king):
        queens,ans=set(tuple(q) for q in queens),[]
        moves=[(0,1),(0,-1),(1,0),(-1,0),(-1,-1),(-1,1),(1,-1),(1,1)]
        for dx,dy in moves:
            x,y=king[0],king[1]
            while 0<=x<8 and 0<=y<8 and (x,y) not in queens:
                x,y=x+dx,y+dy
            if 0<=x<8 and 0<=y<8:
                ans.append([x,y])
        return ans