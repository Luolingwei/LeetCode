
# 思路: 求各个城市间的最短距离即可
# 1 n次dijskra算法
# 2 Floyd算法

class Solution:
    # Solution 1 classic bfs TLE
    # def findTheCity(self, n, edges, distanceThreshold):
    #     def helper(node):
    #         bfs, visited = [], {node}
    #         heapq.heappush(bfs, (0, node))
    #         while bfs:
    #             dist, i = heapq.heappop(bfs)
    #             visited.add(i)
    #             for j in graph[i]:
    #                 newdist = dist + graph[i][j]
    #                 if j not in visited and newdist <= distanceThreshold:
    #                     heapq.heappush(bfs, (newdist, j))
    #         return len(visited)
    #
    #     graph = collections.defaultdict(dict)
    #     resn, resi = float('inf'), -1
    #     for i, j, dist in edges:
    #         graph[i][j] = dist
    #         graph[j][i] = dist
    #
    #     for node in range(n)[::-1]:
    #         n = helper(node)
    #         if n < resn:
    #             resn, resi = n, node
    #     return resi

    # Solution 2 Floyd algorithm
    def findTheCity(self, n, edges, distanceThreshold):
        dist=[[float('inf')]*n for _ in range(n)]
        for i in range(n): dist[i][i]=0
        for i,j,d in edges:
            dist[i][j]=dist[j][i]=d
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j]=min(dist[i][j],dist[i][k]+dist[k][j])
        resn,resi=float('inf'),-1
        for i in range(n)[::-1]:
            curn=sum(dist[i][j]<=distanceThreshold for j in range(n))
            if curn<resn: resn,resi=curn,i
        return resi

a=Solution()
print(a.findTheCity(4,[[0,1,3],[1,2,1],[1,3,4],[2,3,1]],4))