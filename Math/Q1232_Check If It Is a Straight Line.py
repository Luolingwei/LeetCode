
# 思路: check每两个点之间的斜率，注意竖直的情况斜率无法求出

class Solution:
    def checkStraightLine(self, points):
        def ratio(p1,p2):
            try: return (p2[1]-p1[1])/(p2[0]-p1[0])
            except: return float('inf')
        return all(ratio(points[i-1],points[i])==ratio(points[i],points[i+1]) for i in range(1,len(points)-1))

a=Solution()
print(a.checkStraightLine([[-3,-2],[-1,-2],[2,-2],[-2,-2],[0,-2]]))
print(a.checkStraightLine([[-1,1],[-6,-4],[-6,2],[2,0],[-1,-2],[0,-4]]))