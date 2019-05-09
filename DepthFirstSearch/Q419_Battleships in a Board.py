class Solution:
    # Solution 1: dfs
    # def countBattleships(self, board):
    #     """
    #     :type board: List[List[str]]
    #     :rtype: int
    #     """
    #     self.count=0
    #     visited=set()
    #     def dfs(i,j):
    #         if 0<=i<len(board) and 0<=j<len(board[0]) and (i,j) not in visited and board[i][j]=='X':
    #             visited.add((i,j))
    #             dfs(i-1,j)
    #             dfs(i+1,j)
    #             dfs(i,j-1)
    #             dfs(i,j+1)
    #
    #     for i in range(len(board)):
    #         for j in range(len(board[0])):
    #             if (i,j) not in visited and board[i][j]=='X':
    #                 dfs(i,j)
    #                 self.count+=1
    #     return self.count

    # Solution 2: 只计算左边和上边都为'.'的 'x'个数，即ship的船头，避免了重复.
    def countBattleships(self, board):
        ships=0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]=='X' and ((i==0 or board[i-1][j]=='.') and (j==0 or board[i][j-1]=='.')):
                    ships+=1
        return ships

a=Solution()
print(a.countBattleships(['X..X','...X','...X']))
print(a.countBattleships([]))