
# 思路1: union find, 将edge从小到大排序, 依次加入, union成功即加上这个cost, Kruskal算法
# 思路2: 随机选取一个开始点, 每次加入离当前集合最近的一个点, 用dist数组记录并动态更新所有点距离当前集合T的最近距离, Prim算法

class Solution:

    # Solution 1
    # def minCostConnectPoints(self, points):
    #
    #     def dist(e1, e2):
    #         return abs(e1[0] - e2[0]) + abs(e1[1] - e2[1])
    #
    #     def find(x):
    #         while x in uf:
    #             # path compress
    #             while uf[x] in uf:
    #                 uf[x] = uf[uf[x]]
    #             x = uf[x]
    #         return x
    #
    #     def union(x, y):
    #         px, py = find(x), find(y)
    #         if px == py: return False
    #         uf[px] = py
    #         return True
    #
    #     n = len(points)
    #     res = 0
    #     uf = {}
    #     edges = []
    #     for i in range(n):
    #         for j in range(i + 1, n):
    #             edges.append([dist(points[i], points[j]), i, j])
    #
    #     edges.sort()
    #     for cost, x, y in edges:
    #         if union(x, y):
    #             res += cost
    #
    #     return res

    # Solution 2
    def minCostConnectPoints(self, points):
        n, res = len(points), 0
        dist = [float('inf')]*n
        T = {0}
        curp = points[0]
        for _ in range(n-1):
            for i,(x,y) in enumerate(points):
                if i not in T:
                    dist[i] = min(dist[i], abs(curp[0]-x)+abs(curp[1]-y))
            mind, n = min((d,n) for n,d in enumerate(dist))
            res += mind
            dist[n] = float('inf')
            curp = points[n]
            T.add(n)
        return res


a=Solution()
print(a.minCostConnectPoints([[0,0],[2,2],[3,10],[5,2],[7,0]]))
print(a.minCostConnectPoints([[3,12],[-2,5],[-4,1]]))
print(a.minCostConnectPoints([[0,0],[1,1],[1,0],[-1,1]]))
print(a.minCostConnectPoints([[-1000000,-1000000],[1000000,1000000]]))
print(a.minCostConnectPoints([[0,0]]))