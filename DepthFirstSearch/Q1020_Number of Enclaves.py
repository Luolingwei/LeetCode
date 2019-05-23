class Solution:
    def mark(self,board):
        def markStart(i,j):
            nonlocal m,n
            if 0<=i<m and 0<=j<n and board[i][j]==1:
                board[i][j]=0
                markStart(i-1,j)
                markStart(i+1,j)
                markStart(i,j-1)
                markStart(i,j+1)

        m,n=len(board),len(board[0])
        for i in range(m):
            markStart(i,0)
            markStart(i,n-1)
        for j in range(n):
            markStart(0,j)
            markStart(m-1,j)

    def numEnclaves(self, A):
        self.mark(A)
        return sum([sum(i) for i in A])

a=Solution()
print(a.numEnclaves([[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]))
print(a.numEnclaves([[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]))
print(a.numEnclaves([[0]]))