
# 思路: 从右上角往左下角扫描，从上到下找到第一个负数的点，后面都是负数
# 然后向左移动一格，再往下(上面的一定都是正数)
# 终止条件为达到左边界或下边界

class Solution:
    # O(m+n)
    def countNegatives(self, grid):
        m,n=len(grid),len(grid[0])
        r,c=0,n-1
        res=0
        while r<m and c>=0:
            while r<m and grid[r][c]>=0:
                r+=1
            res+=m-r
            c-=1
        return res