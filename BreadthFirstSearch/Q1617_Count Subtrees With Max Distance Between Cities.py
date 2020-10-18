from collections import defaultdict
from collections import deque

# 思路: 用bitmask找出所有可能的城市组合, 然后用这些城市构建graph
# bfs寻找当前cities的最远距离, 以所有city为中心依次遍历一次
# 如果当前cities有一个不能到达, 则不联通(非subtree), 舍弃

class Solution:
    def countSubgraphsForEachDiameter(self, n: int, edges):

        def bfs(c,graph):
            q, visited = deque([(c,0)]), {c}
            dist = 0
            while q:
                c, curd = q.popleft()
                dist = curd
                for nextc in graph[c]:
                    if nextc not in visited:
                        q.append((nextc,curd+1))
                        visited.add(nextc)
            return dist, visited

        def maxDist(cities):
            graph = defaultdict(list)
            for x, y in edges:
                if x in cities and y in cities:
                    graph[x].append(y)
                    graph[y].append(x)

            maxd = 0
            for c in cities:
                dist, visited = bfs(c,graph)
                if len(visited)!=len(cities): return 0
                maxd = max(dist, maxd)
            return maxd

        res = [0]*(n-1)
        for mask in range(1, 1<<(n)):
            cities = []
            for i in range(1, n+1):
                if mask&(1<<(i-1)):
                    cities.append(i)
            maxd = maxDist(cities)
            if maxd>0:
                res[maxd-1] += 1
        return res


a=Solution()
print(a.countSubgraphsForEachDiameter(4, [[1,2],[2,3],[2,4]]))
print(a.countSubgraphsForEachDiameter(2, [[1,2]]))
print(a.countSubgraphsForEachDiameter(3, [[1,2],[2,3]]))