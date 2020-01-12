
# 思路: 寻找group的数量即可，用dfs从0到n-1搜索，用数组记录visited的节点

import collections
class Solution:
    def makeConnected(self, n: int, connections):
        if len(connections) < n - 1:
            return -1
        graph = collections.defaultdict(list)
        for i, j in connections:
            graph[i].append(j)
            graph[j].append(i)

        def dfs(i):
            if not visited[i]:
                visited[i] = 1
                for nexti in graph[i]:
                    dfs(nexti)

        visited = [0] * n
        res = 0
        for i in range(n):
            if not visited[i]:
                dfs(i)
                res += 1
        return res - 1

a=Solution()
print(a.makeConnected(6,[[0,1],[0,2],[0,3],[1,2],[1,3]]))
print(a.makeConnected(5,[[0,1],[0,2],[3,4],[2,3]]))