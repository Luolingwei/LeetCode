# Example 1:
# Input: [[1,3], [0,2], [1,3], [0,2]]
# Output: true
# Explanation:
# The graph looks like this:
# 0----1
# |    |
# |    |
# 3----2
# We can divide the vertices into two groups: {0, 2} and {1, 3}.

# 涂色问题，Same as Q886，先构建关系图(此题已构建完成)，每进入一个区开始涂色，遇到已涂的且颜色不一致就返回False,遍历所有节点并涂色.

import collections
class Solution:
    # solution 1 dfs 44 ms
    def isBipartite(self, graph):
        dic_color={}
        def dfs(node,color):
            if node in dic_color:
                return dic_color[node]==color
            dic_color[node]=color
            for next_node in graph[node]:
                if not dfs(next_node,-color):
                    return False
            return True
        for node in range(len(graph)):
            if not any([node in dic_color,dfs(node,1)]):
                return False
        return True

    # solution 2 bfs 44 ms
    # def isBipartite(self, graph):
    #     dic_color={}
    #     for i in range(len(graph)):
    #         if i not in dic_color:
    #             queue=[(i,1)]
    #             dic_color[i]=1
    #             while queue:
    #                 node,color=queue.pop(0)
    #                 for next_node in graph[node]:
    #                     if next_node in dic_color:
    #                         if dic_color[next_node]!=-color:
    #                             return False
    #                     else:
    #                         queue.append((next_node,-color))
    #                         dic_color[next_node]=-color
    #     return True


a=Solution()
print(a.isBipartite([[1,3], [0,2], [1,3], [0,2]]))
print(a.isBipartite([[1,2,3], [0,2], [0,1,3], [0,2]]))