# Input: [[1,2], [2,3], [3,4], [1,4], [1,5]]
# Output: [1,4]
# Explanation: The given undirected graph will be like this:
# 5 - 1 - 2
#     |   |
#     4 - 3

# 思路1: dfs，在构建图的过程中先判断两个是否已经相连(回构成环路)，如果是，返回当前edge.
# 思路2: Union Find，查到第一个形成环路(两节点有相同祖先)的edge时，返回该edge.

import collections
class Solution:
    # Solution 1 dfs 52 ms
    # def findRedundantConnection(self, edges):
    #     def dfs(x,y,visited):
    #         if y in conn[x]:
    #             return True
    #         visited.add(x)
    #         for u in conn[x]:
    #             if u not in visited:
    #                 visited.add(u)
    #                 if dfs(u,y,visited):
    #                     return True
    #                 visited.remove(u)
    #         return False
    #
    #     conn=collections.defaultdict(dict)
    #     for u,v in edges:
    #         if u in conn and v in conn:
    #             if dfs(u,v,set()): return [u,v]
    #         conn[u][v]=1
    #         conn[v][u]=1


    # Solution 2 Union Find 44ms
    def findRedundantConnection(self, edges):
        def find(x):
            while x in uf:
                # path compress
                while uf[x] in uf:
                    uf[x] = uf[uf[x]]
                x = uf[x]
            return x

        def union(x, y):
            px, py = find(x), find(y)
            if px == py: return False
            uf[px] = py
            return True

        uf = {}
        for x, y in edges:
            if not union(x, y):
                return [x, y]

a=Solution()
print(a.findRedundantConnection([[1,2], [2,3], [3,4], [1,4], [1,5]]))