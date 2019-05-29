
# 思路: 向量解法，首先将坐标按照 x[0], x[1]排序，然后生成向量，判断向量的模是否相等，然后判断其中一个角是否为直角（向量的点积）

class Solution:
    def validSquare(self, p1, p2, p3, p4):
        def vector(point1,point2):
            return [point2[0]-point1[0],point2[1]-point1[1]]
        def distance(vector):
            return vector[0]**2+vector[1]**2
        points=sorted([p1,p2,p3,p4],key=lambda x:(x[0],x[1]))
        if any([points[0]==points[1],points[1]==points[2],points[2]==points[3]]): return False
        vector12,vector24,vector43,vector31=vector(points[0],points[1]),vector(points[1],points[3]),vector(points[3],points[2]),vector(points[2],points[0])
        return distance(vector12)==distance(vector24)==distance(vector43)==distance(vector31) and vector12[0]*vector24[0]+vector12[1]*vector24[1]==0

a=Solution()
print(a.validSquare([0,0],[1,1],[1,0],[0,1]))
print(a.validSquare([1,0],[-1,0],[0,1],[0,-1]))
print(a.validSquare([0,0],[0,0],[0,0],[0,0]))