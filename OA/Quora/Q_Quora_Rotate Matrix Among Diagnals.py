class Solution:
    def rotate(self,matrix,k):
        A=[m[:] for m in matrix]
        N=len(A)
        def once():
            for i in range(N//2):
                A[i],A[N-1-i]=A[N-1-i],A[i]
            for i in range(N):
                for j in range(i+1,N):
                    A[i][j],A[j][i]=A[j][i],A[i][j]
        for _ in range(k):
            once()
        for i in range(N):
            A[i][i],A[i][N-1-i]=matrix[i][i],matrix[i][N-1-i]
        return A

a=Solution()
print(a.rotate([[1, 2, 3],
[4, 5, 6],
[7, 8, 9]]
,2))
print(a.rotate(
[[1,2,3,4,5],
[6,7,8,9,10],
[11,12,13,14,15],
[16,17,18,19,20],
[21,22,23,24,25]]
,1))