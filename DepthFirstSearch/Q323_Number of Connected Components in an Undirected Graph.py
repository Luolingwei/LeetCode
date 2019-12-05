import collections
class Solution:
    def countComponents(self, n, edges):
        visited = set()
        res = 0
        graph = collections.defaultdict(list)
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)

        def dfs(i):
            visited.add(i)
            for nextnode in graph[i]:
                if nextnode not in visited:
                    dfs(nextnode)

        for i in range(n):
            if i not in visited:
                dfs(i)
                res += 1
        return res
