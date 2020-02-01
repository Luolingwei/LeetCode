
# 思路1: 从每个度为1的node开始bfs，每次move一个单位，直到bfs为空
# 思路2: 从边缘开始剪枝，直到剩下不到2个节点，剪枝次数乘2即为最长路径

import collections
class Solution:
    # Solution 1 bfs 468 ms
    # def treeDiameter(self, edges):
        # graph=collections.defaultdict(set)
        # for i,j in edges:
        #     graph[i].add(j)
        #     graph[j].add(i)
        # bfs=[(node,None) for node,next in graph.items() if len(next)==1]
        # move=0
        # while bfs:
        #     bfs=[(next,node) for node,pre in bfs for next in graph[node] if next!=pre]
        #     move+=1
        # return move

    # Solution 2 tree prune 188 ms
    def treeDiameter(self, edges):
        graph=collections.defaultdict(set)
        degree=collections.defaultdict(int)

        for i,j in edges:
            graph[i].add(j)
            graph[j].add(i)
            degree[i]+=1
            degree[j]+=1

        leaves=[i for i,d in degree.items() if d==1]
        move=0
        while len(leaves)>=2:
            new_leaves=[]
            for leaf in leaves:
                degree[leaf]=0
                for node in graph[leaf]:
                    degree[node]-=1
                    if degree[node]==1:
                        new_leaves.append(node)
            leaves=new_leaves
            move+=1
        return 2*move-(not leaves)

a=Solution()
print(a.treeDiameter([[0,1],[1,2],[2,3],[1,4],[4,5]]))
print(a.treeDiameter([[0,1],[0,2]]))
print(a.treeDiameter([[0,1],[0,2],[1,3]]))
print(a.treeDiameter([[0,1],[1,2],[0,3],[3,4],[2,5],[3,6]]))