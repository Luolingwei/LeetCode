
# 思路: 计算每行每列的server个数，如果一个server与其他server连接，则该行或该列server个数大于1

class Solution:
    # O(mn)
    def countServers(self, grid):
        res=0
        m,n=len(grid),len(grid[0])
        row,col=list(map(sum,grid)),list(map(sum,zip(*grid)))
        for i in range(m):
            for j in range(n):
                if grid[i][j] and (row[i]>1 or col[j]>1):
                    res+=1
        return res

a=Solution()
print(a.countServers([[1,0],[0,1]]))