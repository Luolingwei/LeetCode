
# 思路: 用矩阵存行，列，对角线元素个数即可，对角线只存最长的对角线

class TicTacToe:
    def __init__(self, n: int):
        self.rows=[[0]*n,[0]*n]
        self.cols=[[0]*n,[0]*n]
        self.diag1=[0,0]
        self.diag2=[0,0]
        self.N=n

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).8
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        p=player-1
        self.rows[p][row]+=1
        self.cols[p][col]+=1
        self.diag1[p]+=(row==col)
        self.diag2[p]+=(row+col==self.N-1)
        if self.N in (self.rows[p][row],self.cols[p][col],self.diag1[p],self.diag2[p]):
            return player
        else:
            return 0