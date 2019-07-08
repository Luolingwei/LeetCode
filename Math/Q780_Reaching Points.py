# Examples:
# Input: sx = 1, sy = 1, tx = 3, ty = 5
# Output: True
# Explanation:
# One series of moves that transforms the starting point to the target is:
# (1, 1) -> (1, 2)
# (1, 2) -> (3, 2)
# (3, 2) -> (3, 5)
#
# Input: sx = 1, sy = 1, tx = 2, ty = 2
# Output: False
#
# Input: sx = 1, sy = 1, tx = 1, ty = 1
# Output: True

# 思路: 从后往前考虑，tx,ty一定是从(tx-n*ty,ty) or (tx,ty-n*tx)变换过来的，n>=1.
# 考虑到ty-n*tx>=0，所以当ty>tx时候，一定是加了ty，ty<tx的时候，一定是加了tx.
# 回退的时候每次减去n个tx或者ty，n=ty//tx，(减到正好ty<tx)
# 同时要保证减后的值大于等于sx,sy, 所以减去的个数n=(ty-sy)//tx
# 如果ty-sy不够tx了，n=0，但是还是要减去1个tx，此时ty<sy，返回False

class Solution:
    def reachingPoints(self, sx, sy, tx, ty):
        while tx>=sx and ty>=sy:
            if tx==sx and ty==sy: return True
            if ty>tx:
                n=max(1,(ty-sy)//tx)
                ty-=n*tx
            else:
                n=max(1,(tx-sx)//ty)
                tx-=n*ty
        return False

a=Solution()
print(a.reachingPoints(1,1,3,5))
print(a.reachingPoints(1,1,1,1))
print(a.reachingPoints(1,1,2,2))
print(a.reachingPoints(35,13,56367,420098884))