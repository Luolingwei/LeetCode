from collections import deque

# 思路: yi + yj + |xi - xj| = xj + yj + yi - xi
# 对于每个 (xj + yj), 需要找到距离xj在k以内的点(xi,yi)使得yi-xi最大
# 对于(xj, yj), 用单调队列维护其前面k范围内的(yi-xi), 每次取q[0]的yi-xi即可
# 若q[0]的xi距离当前xj超过了k, pop出来直到找到合适的xi

class Solution:
    def findMaxValueOfEquation(self, points, k):
        res = float('-inf')
        q = deque()
        for p in points:
            x, y, dxy = p[0], p[1], p[1] - p[0]
            while q and x - q[0][1] > k: q.popleft()
            if q: res = max(res, q[0][0] + x + y)
            while q and dxy>q[-1][0]:
                q.pop()
            q.append((dxy, x))
        return res


a=Solution()
print(a.findMaxValueOfEquation([[1,3],[2,0],[5,10],[6,-10]],1))
print(a.findMaxValueOfEquation([[0,0],[3,0],[9,2]],3))
print(a.findMaxValueOfEquation([[-17,5],[-10,-8],[-5,-13],[-2,7],[8,-14]], 4))