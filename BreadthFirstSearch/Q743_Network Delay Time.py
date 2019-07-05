# Input: times = [[2,1,1],[2,3,1],[3,4,1]], N = 4, K = 2
# Output: 2

# 思路: 每次pop出当前跑的最快(t最小)的节点，并加入visited，用not in visited筛掉已经遍历的节点(用时更长)
# 依次遍历所有连接的节点，并记录最后一个访问的节点的时间t作为ans，如果没有访问到所有的节点，返回-1

import heapq
import collections
class Solution:
    def networkDelayTime(self, times, N, K):
        graph,ans=collections.defaultdict(dict),0
        for u,v,t in times:
            graph[u][v]=t
        bfs,visited=[(0,K)],set()
        while bfs:
            t,node=heapq.heappop(bfs)
            if node not in visited:
                ans=t
                visited.add(node)
                for next_node in graph[node]:
                    heapq.heappush(bfs,(t+graph[node][next_node],next_node))
        return ans if len(visited)==N else -1

a=Solution()
print(a.networkDelayTime([[2,1,1],[2,3,1],[3,4,1]],4,2))
print(a.networkDelayTime([[1,2,1],[2,3,2],[1,3,4]],3,1))
print(a.networkDelayTime([[1,2,2],[1,3,3]],3,1))