
# 先构建小于最大值的primes table，然后spirial遍历matrix

class Solution:
    def SpiralFind(self,matrix):
        def primes(N):
            table=[1]*N
            table[0],table[1]=0,0
            for i in range(2,int(N**0.5)+1):
                for j in range(i*i,N,i):
                    table[j]=0
            return table

        tableP=primes(10001)
        m,n=len(matrix),len(matrix and matrix[0])
        if not m or not n: return []
        visited=[[0]*n for _ in range(m)]
        moves=[(0,1),(1,0),(0,-1),(-1,0)]
        x,y,i,ans=0,0,0,[]

        while not visited[x][y]:
            visited[x][y]=1
            if tableP[matrix[x][y]]: ans.append(matrix[x][y])
            newx,newy=x+moves[i][0],y+moves[i][1]
            if 0<=newx<m and 0<=newy<n and not visited[newx][newy]:
                x,y=newx,newy
            else:
                i=(i+1)%4
                x,y=x+moves[i][0],y+moves[i][1]
                if x<0 or x>=m or y<0 or y>=n: break
        return ans

a=Solution()
print(a.SpiralFind([[7,7,3,8,1],[13,5,4,5,2],[9,2,12,3,9],[6,12,1,11,41]]))