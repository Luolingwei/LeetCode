
# 思路: 对于每个元素寻找横向或纵向下3个的abs(val), 如果一样, 标记为负, 遍历下来后所有连续超过3个一样的元素都会标记为负
# 如果某一轮找到有可以eliminate的元素, 对于每一列将整数从底向上填充, 最后上面都填为0即可

class Solution:
    def candyCrush(self, board):
        m, n = len(board), len(board[0])
        found = True
        while found:
            found = False
            for i in range(m):
                for j in range(n):
                    if board[i][j] == 0: continue
                    val = abs(board[i][j])
                    if i+2<m and abs(board[i+1][j]) == val and abs(board[i+2][j]) == val:
                        found = True
                        for k in range(i,i+3): board[k][j] = -val
                    if j+2<n and abs(board[i][j+1]) == val and abs(board[i][j+2]) == val:
                        found = True
                        for k in range(j,j+3): board[i][k] = -val
            if found:
                for j in range(n):
                    to_fill = m-1
                    for i in range(m-1,-1,-1):
                        if board[i][j]>0:
                            board[to_fill][j] = board[i][j]
                            to_fill-=1
                    for i in range(to_fill, -1, -1): board[i][j] = 0
        return board


a=Solution()
print(a.candyCrush([[110,5,112,113,114],[210,211,5,213,214],[310,311,3,313,314],[410,411,412,5,414],[5,1,512,3,3],[610,4,1,613,614],[710,1,2,713,714],[810,1,2,1,1],[1,1,2,2,2],[4,1,4,4,1014]]))