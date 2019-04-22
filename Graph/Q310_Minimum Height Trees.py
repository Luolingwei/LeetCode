# Input: n = 6, edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]
#
#      0  1  2
#       \ | /
#         3
#         |
#         4
#         |
#         5
#
# Output: [3, 4]

# 思路:想象成一个圈，返回的结果一定是最中心的节点，（到四周的最长距离最短），所以从树的外层进行剪枝，直到剩下的节点为1个或者2个，就是需要的答案
class Solution:
    def findMinHeightTrees(self, n, edges):
        if n==1: return [0]
        graph=[[] for _ in range(n)]
        degree=[0]*n

        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
            degree[edge[0]]+=1
            degree[edge[1]]+=1

        leaves=[i for i in range(n) if degree[i]==1]

        nodes=n
        while nodes>2:
            new_leaves=[]
            for leaf in leaves:
                degree[leaf]=0
                nodes-=1
                for node in graph[leaf]:
                    degree[node]-=1
                    if degree[node]==1:
                        new_leaves.append(node)
            leaves=new_leaves
        return leaves

a=Solution()
print(a.findMinHeightTrees(6,[[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]))
print(a.findMinHeightTrees(4,[[1, 0], [1, 2], [1, 3]]))
print(a.findMinHeightTrees(2,[[1,0]]))
print(a.findMinHeightTrees(1,[[0]]))