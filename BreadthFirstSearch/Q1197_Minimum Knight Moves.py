
# 思路: 利用对称性，只考虑第一象限的target，只要这个能到，利用其它方向一定能到原来的target
# 排除两个方向(-2,-1)和(-1,-2), 剩下6个，其中4个用来处理(0,100),(100,0)之类的corner case
# 但是在bfs的过程中x和y不能超过-2, 因为我们的target x>=0 y>=0，超过-2的move是多余的

class Solution:
    def minKnightMoves(self, x, y):
        x,y=abs(x),abs(y)
        bfs,visited={(0,0)},{(0,0)}
        moves=0
        while bfs:
            new_bfs=set()
            for i,j in bfs:
                if (i,j)==(x,y): return moves
                for di,dj in [(2,-1),(1,-2),(-2,1),(-1,2),(1,2),(2,1)]:
                    newi,newj=i+di,j+dj
                    if newi>=-2 and newj>=-2 and (newi,newj) not in visited:
                        new_bfs.add((newi,newj))
            bfs=new_bfs
            moves+=1
            visited|=bfs

a=Solution()
print(a.minKnightMoves(2,1))
print(a.minKnightMoves(5,5))
print(a.minKnightMoves(270,-21))