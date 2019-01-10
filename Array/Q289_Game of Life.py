class Solution(object):
    def get_live(self,board,i,j):
        lives=0
        for x in range(i-1,i+2):
            for y in range(j-1,j+2):
                if x!=i or y!=j:
                    if -1<x<len(board) and -1<y<len(board[0]):
                        lives+=board[x][y]
        return lives

    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        board_copy=[[val for val in board[i]] for i in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.get_live(board_copy,i,j)==3:
                    board[i][j]=1
                elif self.get_live(board_copy,i,j)==2 and board_copy[i][j]==1:
                    board[i][j]=1
                else:
                    board[i][j]=0
        return board

a=Solution()
print(a.gameOfLife([
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]))