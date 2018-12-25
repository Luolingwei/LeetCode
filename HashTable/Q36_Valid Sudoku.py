class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        row_set=[[] for _ in range(9)]
        col_set=[[] for _ in range(9)]
        grod_set=[[] for _ in range(9)]

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]=='.':
                    continue
                num=board[i][j]
                grid=i//3*3+j//3
                if num in row_set[i] or num in col_set[j] or num in grod_set[grid]:
                    return False
                else:
                    row_set[i].append(num)
                    col_set[j].append(num)
                    grod_set[grid].append(num)
        return True

a=Solution()
print(a.isValidSudoku([
  ["0","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]))

