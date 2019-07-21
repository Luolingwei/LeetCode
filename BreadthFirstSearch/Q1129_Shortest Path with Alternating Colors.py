# Input: n = 3, red_edges = [[0,1],[1,2]], blue_edges = []
# Output: [0,1,-1]

# Input: n = 3, red_edges = [[0,1],[0,2]], blue_edges = [[1,0]]
# Output: [0,1,1]

# 思路: 将路径都加上颜色，当颜色与上一个重复时，不继续往下走
# 这里visited为了防止环路导致的死循环，记录节点和颜色状态，注意同一节点的不同颜色不算重复，因为可能走环路回来换颜色才能到达某些节点

class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges, blue_edges):
        ans,visited=[-1]*n,{(0,'inf')}
        graph=[[] for _ in range(n)]
        for u,v in red_edges:
            graph[u].append((v,1))
        for u,v in blue_edges:
            graph[u].append((v,-1))
        queue=[(0,'inf',0)]
        while queue:
            new=[]
            for node,color,dist in queue:
                if ans[node]==-1:
                    ans[node]=dist
                for next_node, new_color in graph[node]:
                    if new_color!=color and (next_node,new_color) not in visited:
                        new.append((next_node,new_color,dist+1))
                        visited.add((next_node,new_color))
            queue=new
        return ans

a=Solution()
print(a.shortestAlternatingPaths(3,[[0,1],[1,2]],[]))
print(a.shortestAlternatingPaths(3,[[0,1],[0,2]],[[1,0]]))
print(a.shortestAlternatingPaths(3,[[0,1]],[[1,2]]))
print(a.shortestAlternatingPaths(3,[[1,0]],[[2,1]]))
print(a.shortestAlternatingPaths(3,[[0,1]],[[2,1]]))
print(a.shortestAlternatingPaths(5,[[0,1],[1,2],[2,3],[3,4]],[[1,2],[2,3],[3,1]]))