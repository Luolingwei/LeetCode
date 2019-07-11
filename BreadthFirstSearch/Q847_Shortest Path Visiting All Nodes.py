# Input: [[1,2,3],[0],[0],[0]]
# Output: 4
# Explanation: One possible path is [1,0,2,0,3]

# 思路: 用位运算符记录当前访问的状态，并用memo记录已经访问过的状态

class Solution:
    def shortestPathLength(self, graph):
        N,memo=len(graph),set()
        mindegree=min(len(u) for u in graph)
        starts=[i for i in range(N) if len(graph[i])==mindegree]
        bfs,target=[(start,1<<start,0) for start in starts],(1<<N)-1
        while True:
            node,visited,dist=bfs.pop(0)
            if visited==target: return dist
            for next_node in graph[node]:
                if (next_node,visited|1<<next_node) not in memo:
                    bfs.append((next_node,visited|1<<next_node,dist+1))
                    memo.add((next_node,visited|1<<next_node))

a=Solution()
print(a.shortestPathLength([[1,2,3],[0],[0],[0]]))
print(a.shortestPathLength([[1],[0,2,4],[1,3,4],[2],[1,2]]))
print(a.shortestPathLength([[1],[0,2,4],[1,3],[2],[1,5],[4]]))