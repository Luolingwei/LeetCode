class Solution:
    def allPathsSourceTarget(self, graph):
        N,ans=len(graph),[]
        def dfs(pos,path):
            if pos==N-1:
                ans.append(path)
                return
            for node in graph[pos]:
                dfs(node,path+[node])
        dfs(0,[0])
        return ans

a=Solution()
print(a.allPathsSourceTarget([[1,2], [3], [3], []]))