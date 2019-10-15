
from copy import deepcopy

class Solution:
    def GridGame(self,matrix,rules,k):
        trans={"dead":0,"alive":1}
        newrule=[trans[r] for r in rules]
        m,n=len(matrix),len(matrix[0])
        moves=[(0,1),(1,0),(0,-1),(-1,0),(1,1),(-1,-1),(1,-1),(-1,1)]
        for _ in range(k):
            new_matrix=deepcopy(matrix)
            for i in range(m):
                for j in range(n):
                    candidates=[(i+dx,j+dy) for dx,dy in moves if 0<=i+dx<m and 0<=j+dy<n]
                    new_matrix[i][j]=newrule[sum(matrix[x][y] for x,y in candidates)]
            matrix=new_matrix
        return matrix

a=Solution()
print(a.GridGame([[0,1,1,0],[1,1,0,0]],["dead","dead","dead","alive","dead","alive","dead","dead","dead"],1))