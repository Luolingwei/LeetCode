class Solution:
    def markFromBoard(self,board,i,j,m,n):
        if -1<i<m and -1<j<n and board[i][j]=='O':
            board[i][j]='Safe'
        else: return
        self.markFromBoard(board,i-1,j,m,n)
        self.markFromBoard(board,i+1,j,m,n)
        self.markFromBoard(board,i,j-1,m,n)
        self.markFromBoard(board,i,j+1,m,n)

    def mark(self,board,m,n):
        for i in range(m):
            self.markFromBoard(board,i,0,m,n)
            self.markFromBoard(board,i,n-1,m,n)
        for j in range(n):
            self.markFromBoard(board,0,j,m,n)
            self.markFromBoard(board,m-1,j,m,n)

    def solve(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        m=len(board)
        n=len(board[0]) if m else 0
        self.mark(board,m,n)
        for i in range(m):
            for j in range(n):
                if board[i][j]=='Safe':
                    board[i][j]='O'
                else:
                    board[i][j]='X'
        return board

a=Solution()
print(a.solve([['X','X','X','X'],['X','O','O','X'],['X','X','O','X'],['X','O','X','X']]))
print(a.solve([]))