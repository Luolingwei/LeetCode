from collections import defaultdict

# 思路: 找到端点(只有1个相邻的num), 然后根据邻接关系进行拼接

class Solution:
    def restoreArray(self, adjacentPairs):
        memo = defaultdict(list)
        start = None
        N = len(adjacentPairs)+1
        for x,y in adjacentPairs:
            memo[x].append(y)
            memo[y].append(x)
        for k in memo.keys():
            if len(memo[k])==1:
                start = k
                break
        res = [start]
        visited = {start}
        while len(res)<N:
            for nextnode in memo[start]:
                if nextnode not in visited:
                    start = nextnode
                    visited.add(nextnode)
                    res.append(nextnode)
        return res


a=Solution()
print(a.restoreArray([[2,1],[3,4],[3,2]]))
print(a.restoreArray([[4,-2],[1,4],[-3,1]]))
print(a.restoreArray([[100000,-100000]]))