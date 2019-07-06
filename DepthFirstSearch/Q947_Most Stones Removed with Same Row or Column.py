# Input: stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
# Output: 5

# 思路: dfs，类似寻找island，但是这里的点不一定是相邻的，而是在同一行或者同一列，找出总共有多少个island即可(最少剩的个数).

import collections
class Solution:
    def removeStones(self, stones):
        points,visited,island={(x,y) for x,y in stones},set(),0
        def dfs(x,y):
            visited.add((x,y))
            for new_y in row[x]:
                if (x,new_y) not in visited:
                    dfs(x,new_y)
            for new_x in columns[y]:
                if (new_x,y) not in visited:
                    dfs(new_x,y)
        row,columns=collections.defaultdict(set),collections.defaultdict(set)
        for u,v in stones:
            row[u].add(v)
            columns[v].add(u)
        for i,j in stones:
            if (i,j) not in visited:
                dfs(i,j)
                island+=1
        return len(stones)-island

a=Solution()
print(a.removeStones([[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]))