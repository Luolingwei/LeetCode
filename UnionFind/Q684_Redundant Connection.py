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
            if uf[x]!=x: return find(uf[x])
            return x
        N=len(edges)
        uf={i:i for i in range(1,N+1)} # or uf=list(range(N+1))
        for u,v in edges:
            if find(u)==find(v): return [u,v]
            else: uf[find(u)]=find(v)
        return []

a=Solution()
print(a.findRedundantConnection([[1,2], [2,3], [3,4], [1,4], [1,5]]))