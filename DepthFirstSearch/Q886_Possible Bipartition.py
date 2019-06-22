# Input: N = 4, dislikes = [[1,2],[1,3],[2,4]]
# Output: true
# Explanation: group1 [1,4], group2 [2,3]

# 思路: dfs 或者 bfs，先构建相关关系的graph，然后用bfs/dfs搜索每一个node（带上color），每次进行到下一轮的bfs/dfs时将color改为-color
# 当遇到color中有的node时，判断颜色是否与当前颜色相等，返回(回访问题在这里被一并处理，回访的case一定为True)
# Note: 可以把图考虑成几个不相邻的色块，每碰到一个色块，初始化颜色1开始涂色，直到色块涂完并没有碰到冲突的颜色,

import collections
class Solution:
    # solution 1 dfs 176 ms
    def possibleBipartition(self, N, dislikes):
        def dfs(node,color):
            if node in dic_color:
                return color==dic_color[node]
            dic_color[node]=color
            for next_node in graph[node]:
                if not dfs(next_node,-color):
                    return False
            return True

        graph=collections.defaultdict(set)
        dic_color={}
        for u,v in dislikes:
            graph[u].add(v)
            graph[v].add(u)

        for node in range(1,N+1):
            if not node in dic_color and not dfs(node,1):
                return False
        return True


    # solution 2 bfs 168 ms
    # def possibleBipartition(self, N, dislikes):
    #     graph=collections.defaultdict(set)
    #     dic_color={}
    #     for u,v in dislikes:
    #         graph[u].add(v)
    #         graph[v].add(u)
    #
    #     for i in range(1,N+1):
    #         if i not in dic_color:
    #             queue=[(i,1)]
    #             while queue:
    #                 node,color=queue.pop(0)
    #                 for next_node in graph[node]:
    #                     if next_node in dic_color:
    #                         if dic_color[next_node]!=-color:
    #                             return False
    #                     else:
    #                         dic_color[next_node]=-color
    #                         queue.append((next_node,-color))
    #     return True

a=Solution()
print(a.possibleBipartition(4,[[1,2],[1,3],[2,4]]))
print(a.possibleBipartition(3,[[1,2],[1,3],[2,3]]))
print(a.possibleBipartition(5,[[1,2],[2,3],[3,4],[4,5],[1,5]]))