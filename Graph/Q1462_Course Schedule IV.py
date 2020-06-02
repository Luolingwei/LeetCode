from collections import defaultdict

# 思路1: 构建图, dfs判断i是否能到j, 用memo对(i,j)进行cache

# 思路2: floyd算法.

class Solution:
    def checkIfPrerequisite(self, n, prerequisites, queries):
        graph = defaultdict(list)
        for u, v in prerequisites:
            graph[u].append(v)

        def dfs(i, j):
            if i == j:
                return True
            visited.add(i)
            for nei in graph[i]:
                if nei not in visited and dfs(nei, j):
                    return True
            return False

        res = []
        memo = {}
        for i, j in queries:
            visited = set()
            if (i, j) not in memo:
                memo[(i, j)] = dfs(i, j)
            res.append(memo[(i, j)])
        return res


    # def checkIfPrerequisite(self, n, prerequisites, queries):
    #     conn = [[0]*n for _ in range(n)]
    #     for u,v in prerequisites:
    #         conn[u][v] = 1
    #     for k in range(n):
    #         for i in range(n):
    #             for j in range(n):
    #                 if conn[i][k] and conn[k][j]:
    #                     conn[i][j]=1
    #     return [conn[x][y] for x,y in queries]


a=Solution()
print(a.checkIfPrerequisite(5,[[1,2],[1,0],[2,0]],[[1,0],[1,2]]))