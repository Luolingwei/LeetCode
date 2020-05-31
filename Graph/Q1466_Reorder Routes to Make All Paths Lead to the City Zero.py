from collections import defaultdict

# 思路: 因为n个节点n-1个edge形成了树的结构, 所以没有环路, 从0开始bfs即可
# 0往外走, reverse[0]代表这些相邻节点可以到0, 直接加入q
# graph[0]代表0可以到这些相邻节点, 需要翻转, 并加入q
# visited记录已经走过的节点, 防止回访, 直到所有节点已访问

class Solution:
    def minReorder(self, n, connections):
        graph = defaultdict(list)
        reverse = defaultdict(list)
        for u,v in connections:
            graph[u].append(v)
            reverse[v].append(u)
        q,res = [0],0
        visited = {0}
        while q:
            newq = set()
            for node in q:
                for nei in graph[node]:
                    if nei not in visited:
                        res += 1
                        newq.add(nei)
                for nei in reverse[node]:
                    if nei not in visited:
                        newq.add(nei)
            q = newq
            visited|=q
        return res


a=Solution()
print(a.minReorder(6,[[0,1],[1,3],[2,3],[4,0],[4,5]]))
print(a.minReorder(5,[[1,0],[1,2],[3,2],[3,4]]))
print(a.minReorder(3,[[1,0],[2,0]]))