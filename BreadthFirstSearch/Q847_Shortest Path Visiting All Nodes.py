# Input: [[1,2,3],[0],[0],[0]]
# Output: 4
# Explanation: One possible path is [1,0,2,0,3]

# 思路: 用位运算符记录当前visited的状态，并用memo记录已经访问过的相同状态(当前node和visited都相同)，减少bfs次数

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


    def shortestPathLength2(self, graph):
        N = len(graph)
        target = (1 << N) - 1
        min_D = min(len(g) for g in graph)
        starts = [i for i in range(N) if len(graph[i]) == min_D]
        memo = [[-1] * (1 << N) for _ in range(N)]

        def dfs(i, visited):
            if memo[i][visited] > 0: return memo[i][visited]
            if visited == target: return 0
            res = float('inf')
            for next_i in graph[i]:
                if (next_i, visited | 1 << next_i) not in seen:
                    seen.add((next_i, visited | (1 << next_i)))
                    res = min(res, dfs(next_i, visited | 1 << next_i) + 1)
                    seen.remove((next_i, visited | 1 << next_i))
            memo[i][visited] = res
            return res


        res = float('inf')
        for start in starts:
            seen = set()
            res = min(res, dfs(start, 1<<start))
        print(memo)
        return res


a=Solution()
print(a.shortestPathLength2([[1,2,3],[0],[0],[0]]))
print(a.shortestPathLength2([[1],[0,2,4],[1,3,4],[2],[1,2]]))
print(a.shortestPathLength2([[1],[0,2,4],[1,3],[2],[1,5],[4]]))