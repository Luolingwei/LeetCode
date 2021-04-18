

class Solution:

    def find(self, n, edges, node):
        graph = [[] for _ in range(n+1)]
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)


        bfs = [(node, None, 0)]
        visited = {node: 0}
        while bfs:
            new_bfs = []
            for node,parent,dist in bfs:
                for next_node in graph[node]:
                    if next_node!=parent:
                        if next_node in visited:
                            return visited[next_node]+dist+1
                        else:
                            new_bfs.append((next_node, node, dist+1))
                            visited[next_node] = dist+1
            bfs = new_bfs

a=Solution()
print(a.find(5, [[1,2],[1,3],[2,3],[3,4],[4,5],[1,5]], 1))
print(a.find(4, [[1,2],[2,3],[3,4],[4,2]], 1))

