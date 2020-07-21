from collections import defaultdict
from collections import Counter

class Solution:
    # 思路1: 构建无向图, 用visited防止回访, 从底部返回当前子树的字符统计Counter
    # def countSubTrees(self, n: int, edges, labels):
    #     graph = defaultdict(list)
    #     res = [0] * n
    #     for u, v in edges:
    #         graph[v].append(u)
    #         graph[u].append(v)
    #
    #     def dfs(node):
    #         curCounter = Counter(labels[node])
    #         for child in graph[node]:
    #             if child not in visited:
    #                 visited.add(child)
    #                 curCounter += dfs(child)
    #         res[node] = curCounter[labels[node]]
    #         return curCounter
    #
    #     visited = {0}
    #     dfs(0)
    #     return res

    # 思路2: 设置(node,parent), 防止回访, 从底部返回当前子树的字符统计Counter
    def countSubTrees(self, n: int, edges, labels):
        graph = defaultdict(list)
        res = [0] * n
        for u, v in edges:
            graph[v].append(u)
            graph[u].append(v)

        def dfs(node, parent):
            curCounter = Counter(labels[node])
            for child in graph[node]:
                if child != parent:
                    curCounter += dfs(child, node)
            res[node] = curCounter[labels[node]]
            return curCounter

        dfs(0, -1)
        return res


a=Solution()
print(a.countSubTrees(4,[[0,2],[0,3],[1,2]],"aeed"))