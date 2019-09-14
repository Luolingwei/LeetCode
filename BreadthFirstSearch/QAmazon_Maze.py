
# 思路: bfs即可，修改遍历过的格点值为0防止回访

class Solution:
    def Maze(self, board):
        if board[0][0]!=1:
            return board[0][0]==9
        m,n=len(board),len(board[0])
        bfs=[(0,0)]
        while bfs:
            newbfs=[]
            for x,y in bfs:
                for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                    i,j=x+dx,y+dy
                    if 0<=i<m and 0<=j<n and board[i][j]!=0:
                        if board[i][j]==9: return True
                        else:
                            newbfs.append((i,j))
                            board[i][j]=0
            bfs=newbfs
        return False

a=Solution()
print(a.Maze([[1,1,1,1,1,1],[1,1,1,1,0,0],[0,0,1,0,0,0],[1,1,1,1,1,1],[1,0,0,0,1,0],[1,1,1,0,9,0]]))
print(a.Maze([[1,0,0,0,0],[1,1,1,1,1],[1,0,0,0,0],[0,0,9,0,0]]))
print(a.Maze([[1,0,0,0,0],[1,1,1,1,1],[1,0,0,0,1],[0,0,9,1,1]]))
print(a.Maze([[1,1,1,1],[1,0,0,0],[1,9,0,0]]))
print(a.Maze([[1,9]]))
print(a.Maze([[9]]))
print(a.Maze([[1]]))
print(a.Maze([[0]]))