
# 思路: 对每个方向进行dp，存储以前一个元素结尾的最长长度，动态更新maxL

class Solution:
    def longestLine(self, M):
        hor,ver,diag,adiag={},{},{},{}
        res,m,n=0,len(M),len(M and M[0])
        for i in range(m):
            for j in range(n):
                if M[i][j] and j>0: hor[(i,j)]=hor[(i,j-1)]+1
                else: hor[(i,j)]=M[i][j]
                if M[i][j] and i>0: ver[(i,j)]=ver[(i-1,j)]+1
                else: ver[(i,j)]=M[i][j]
                if M[i][j] and i>0 and j>0: diag[(i,j)]=diag[(i-1,j-1)]+1
                else: diag[(i,j)]=M[i][j]
                if M[i][j] and i>0 and j+1<n: adiag[(i,j)]=adiag[(i-1,j+1)]+1
                else: adiag[(i,j)]=M[i][j]
                res=max(res,hor[(i,j)],ver[(i,j)],diag[(i,j)],adiag[(i,j)])
        return res

a=Solution()
print(a.longestLine([[0,1,1,0],[0,1,1,0],[0,0,0,1]]))