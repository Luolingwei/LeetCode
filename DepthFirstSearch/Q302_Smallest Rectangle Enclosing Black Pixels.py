
# 思路: dfs搜索找到最大/最小的x,y, 计算围成的面积即可

class Solution:
    def minArea(self, image, x, y):
        m,n = len(image),len(image[0])
        self.minx,self.miny,self.maxx,self.maxy = float('inf'),float('inf'),float('-inf'),float('-inf')
        def dfs(i,j):
            if 0<=i<m and 0<=j<n and image[i][j]=="1":
                self.minx,self.miny,self.maxx,self.maxy = min(self.minx,i),min(self.miny,j),max(self.maxx,i),max(self.maxy,j)
                image[i][j]="0"
                dfs(i+1,j)
                dfs(i-1,j)
                dfs(i,j+1)
                dfs(i,j-1)
        dfs(x,y)
        return (self.maxx-self.minx+1)*(self.maxy-self.miny+1)
