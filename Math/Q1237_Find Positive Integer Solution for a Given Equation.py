
# 思路: 问题等价于在1000x1000的递增矩阵中，寻找A[i][j]==z
# x从1开始增加，y从1000开始减少，直到f(x,y)<=z，x再增加，y只需要继续减少(递增函数)，继续寻找f(x,y)==z

class Solution:
    # O(N) (O(1000))
    def findSolution(self, customfunction, z):
        ans=[]
        x,y=1,1000
        while x<1001 and y>0:
            while y>0 and customfunction.f(x,y)>z: y-=1
            if y>0 and customfunction.f(x,y)==z:
                ans.append([x,y])
            x+=1
        return ans