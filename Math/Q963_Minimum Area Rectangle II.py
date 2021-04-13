
# 思路: 如果有矩形, 那么四个点一定有先后出现顺序, 按顺序遍历p1,p2,p3,p4
# 先出现的为p1, 两边的p2, p3一定可以按顺序遍历到, 生成对面的p4: (x2+x3-x1,y2+y3-y1)
# 如果p1,p2,p3形成直角, 且p4有, 则形成矩形，这样每个矩形只会计算一次 O(N^3)

class Solution:
    def minAreaFreeRect(self, points):
        def dist(p1,p2):
            return ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)**0.5
        memo, n = set((x,y) for x,y in points), len(points)
        res = float('inf')
        for i in range(n):
            x1, y1 = points[i][0], points[i][1]
            for j in range(i+1, n):
                x2, y2 = points[j][0], points[j][1]
                for k in range(j+1, n):
                    x3, y3 = points[k][0], points[k][1]
                    if (x2-x1)*(x3-x1)+(y2-y1)*(y3-y1)==0 and (x2+x3-x1,y2+y3-y1) in memo:
                        res = min(res, dist((x1,y1),(x2,y2))*dist((x1,y1),(x3,y3)))
        return res if res!=float('inf') else 0


a=Solution()
print(a.minAreaFreeRect([[1,2],[2,1],[1,0],[0,1]]))
print(a.minAreaFreeRect([[0,1],[2,1],[1,1],[1,0],[2,0]]))
print(a.minAreaFreeRect([[0,3],[1,2],[3,1],[1,3],[2,1]]))
print(a.minAreaFreeRect([[3,1],[1,1],[0,1],[2,1],[3,3],[3,2],[0,2],[2,3]]))