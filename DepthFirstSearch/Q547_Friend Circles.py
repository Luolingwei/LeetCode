class Solution:
    def findCircleNum(self, M):
        N=len(M)
        visited,count=set(),0
        def dfs(node):
            for j in range(N):
                if M[node][j]==1 and j not in visited:
                    visited.add(j)
                    dfs(j)
        for i in range(N):
            if i not in visited:
                count+=1
                dfs(i)
        return count

a=Solution()
print(a.findCircleNum([[1,1,0],[1,1,0],[0,0,1]]))
print(a.findCircleNum([[1,1,0],[1,1,1],[0,1,1]]))
print(a.findCircleNum([[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]))