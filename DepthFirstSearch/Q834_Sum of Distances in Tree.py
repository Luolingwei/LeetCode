# Input: N = 6, edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
# Output: [8,12,6,10,10,10]
# Explanation:
# Here is a diagram of the given tree:
#   0
#  / \
# 1   2
#    /|\
#   3 4 5
# We can see that dist(0,1) + dist(0,2) + dist(0,3) + dist(0,4) + dist(0,5)
# equals 1 + 1 + 2 + 2 + 2 = 8.  Hence, answer[0] = 8, and so on.

# 思路: dfs以其中一个节点(如0)计算出总距离，并记录所有节点包含的子节点数
# dfs求其他节点的总距离时，dist[i]=dist[root]-count[i](变近了1)+N-count[i](变远了1)
# 注意防止回访，因为是树结构，所以只需要防止父节点，用pre参数即可.

import collections
class Solution:
    def sumOfDistancesInTree(self, N, edges):
        count=[1]*N
        dist=[0]*N
        tree=collections.defaultdict(list)
        for u,v in edges:
            tree[u].append(v)
            tree[v].append(u)

        def dfs_dist0(root,pre):
            for node in tree[root]:
                if node!=pre:
                    dfs_dist0(node,root)
                    count[root]+=count[node]
                    dist[root]+=dist[node]+count[node]

        def dfs_otherdist(root,pre):
            for node in tree[root]:
                if node!=pre:
                    dist[node]=dist[root]-count[node]+N-count[node]
                    dfs_otherdist(node,root)

        dfs_dist0(0,-1)
        dfs_otherdist(0,-1)
        return dist

a=Solution()
print(a.sumOfDistancesInTree(6,[[0,1],[0,2],[2,3],[2,4],[2,5]]))