class Solution:
    def numMovesStones(self, a, b, c):
        stones=sorted([a,b,c])
        if stones[0]+2==stones[2]: return [0,0]
        return [2 if min(stones[2]-stones[1],stones[1]-stones[0])>2 else 1,stones[2]-stones[0]-2]

a=Solution()
print(a.numMovesStones(1,2,5))
print(a.numMovesStones(4,3,2))
print(a.numMovesStones(3,5,1))
print(a.numMovesStones(7,4,1))