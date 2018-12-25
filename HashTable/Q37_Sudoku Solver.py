class Solution:
    def dfs(self, board, stack1):
        if not stack1:
            return
        (x,y)=stack1.pop()
        row_set=[board[x][i] for i in range(9)]
        col_set=[board[j][y] for j in range(9)]
        grid_set=[board[x//3*3+i][y//3*3+j] for i in range(3) for j in range(3)]

        for num in "123456789":
            if not any([num in row_set, num in col_set, num in grid_set]):
                board[x][y]=num
                self.dfs(board,stack1)
                if not stack1: #搞定了就return 没搞定就换数字
                    return
        #仍然没有搞定 先放回去
        board[x][y]='.'
        stack1.append((x,y))

    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        stack1=[(i,j) for i in range(9) for j in range(9) if board[i][j]=='.']
        self.dfs(board,stack1)
        return board

a=Solution()
print(a.solveSudoku([["5","3",".",".","7",".",".",".","."],
                     ["6",".",".","1","9","5",".",".","."],
                     [".","9","8",".",".",".",".","6","."],
                     ["8",".",".",".","6",".",".",".","3"],
                     ["4",".",".","8",".","3",".",".","1"],
                     ["7",".",".",".","2",".",".",".","6"],
                     [".","6",".",".",".",".","2","8","."],
                     [".",".",".","4","1","9",".",".","5"],
                     [".",".",".",".","8",".",".","7","9"]]))