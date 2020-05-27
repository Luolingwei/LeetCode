# Input:
# [[1,1,0],
#  [1,1,0],
#  [0,0,1]]
# Output: 2
# Explanation:The 0th and 1st students are direct friends, so they are in a friend circle.
# The 2nd student himself is in a friend circle. So return 2.

# 思路1: dfs, 每遇到一个新的person，dfs搜索其朋友，朋友的朋友....加入visited，统计有多少个count
# 思路2: union find, 最多有N个朋友圈, 即每人独立, 每union成功一次, 朋友圈减少1个

class Solution:

    # solution 1 dfs 196 ms
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

    # Solution 2 Union Find 208 ms
    def findCircleNum(self, M):
        def find(x):
            while x in uf:
                # path compress
                while uf[x] in uf:
                    uf[x] = uf[uf[x]]
                x = uf[x]
            return x
        def union(x,y):
            px,py = find(x), find(y)
            if px==py: return False
            uf[px] = py
            return True

        N = len(M)
        count, uf = N, {}
        for i in range(N):
            for j in range(N):
                if M[i][j] and union(i,j):
                    count-=1
        return count

a=Solution()
print(a.findCircleNum([[1,1,0],[1,1,0],[0,0,1]]))
print(a.findCircleNum([[1,1,0],[1,1,1],[0,1,1]]))
print(a.findCircleNum([[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]))