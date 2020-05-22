import math

# 思路: 每个圆的位置可以由圆上2点和半径确定, 枚举所有2点的组合
# 如果2点距离大于直径, 则不可能形成圆
# 如果2点距离小于直径, 则计算2个可能的center, 枚举计算落入圆的点数

class Solution:
    def numPoints(self, points, r: int) -> int:
        def helper(p1, p2):
            return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

        def Circle_Center(x1, y1, x2, y2, R):
            if x1 == x2:
                c1, c2 = (y1 + y2) / 2, (y1 - y2) / 2
                y01 = y02 = c1
                x01 = x1 + math.sqrt(R ** 2 - c2 ** 2)
                x02 = x1 - math.sqrt(R ** 2 - c2 ** 2)
            else:
                c1 = (pow(x2, 2) - pow(x1, 2) + pow(y2, 2) - pow(y1, 2)) / 2 / (x2 - x1)
                c2 = (y2 - y1) / (x2 - x1)
                A = 1.0 + pow(c2, 2)
                B = 2 * (x1 - c1) * c2 - 2 * y1
                C = pow((x1 - c1), 2) + pow(y1, 2) - pow(R, 2)
                y01 = (-B + math.sqrt(B * B - 4 * A * C)) / 2 / A
                x01 = c1 - c2 * y01
                y02 = (-B - math.sqrt(B * B - 4 * A * C)) / 2 / A
                x02 = c1 - c2 * y01
            return [(x01, y01), (x02, y02)]

        def nearN(center):
            return sum(helper(center, points[i])<=r+0.0001 for i in range(N))

        N = len(points)
        ans = 0
        for i in range(N):
            for j in range(i + 1, N):
                if helper(points[i], points[j]) > 2 * r:
                    continue
                x1, y1 = points[i]
                x2, y2 = points[j]
                center1, center2 = Circle_Center(x1, y1, x2, y2, r)
                ans = max(ans, nearN(center1), nearN(center2))
        return max(1, ans)


a=Solution()
print(a.numPoints([[-2,0],[2,0],[0,2],[0,-2]],2))
print(a.numPoints([[1,2],[3,5],[1,-1],[2,3],[4,1],[1,3]],2))
print(a.numPoints([[-2,0],[2,0],[0,2],[0,-2]],1))