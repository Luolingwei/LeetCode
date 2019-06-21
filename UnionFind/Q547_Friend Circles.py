# Input:
# [[1,1,0],
#  [1,1,0],
#  [0,0,1]]
# Output: 2
# Explanation:The 0th and 1st students are direct friends, so they are in a friend circle.
# The 2nd student himself is in a friend circle. So return 2.

# 思路1: dfs, 每遇到一个新的person，dfs搜索其朋友，朋友的朋友....加入visited，统计有多少个count
# 思路2: union find, 构建所有人的祖先关系网，然后看一共有多少个祖先.

class Solution:

    # solution 1 dfs 56 ms
    # def findCircleNum(self, M):
    #     N=len(M)
    #     visited,count=set(),0
    #     def dfs(node):
    #         for j in range(N):
    #             if M[node][j]==1 and j not in visited:
    #                 visited.add(j)
    #                 dfs(j)
    #     for i in range(N):
    #         if i not in visited:
    #             count+=1
    #             dfs(i)
    #     return count

    # Solution 2 Union Find 384 ms
    def findCircleNum(self, M):
        N=len(M)
        def find(x):
            if uf[x]!=x: return find(uf[x])
            else: return x
        uf=list(range(N))
        for i in range(N):
            for j in range(N):
                if M[i][j]:
                    uf[find(i)]=find(j)
        return len(set(find(i) for i in range(N)))

a=Solution()
print(a.findCircleNum([[1,1,0],[1,1,0],[0,0,1]]))
print(a.findCircleNum([[1,1,0],[1,1,1],[0,1,1]]))
print(a.findCircleNum([[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]))