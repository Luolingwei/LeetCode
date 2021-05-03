import heapq
from collections import defaultdict

# 思路1: dijkstra, 从head根据时间往下走. O(nlogn)
# 思路2: dfs, time(head) = max(time(subs)) + informT, O(n)

class Solution:
    def numOfMinutes(self, n, headID, manager, informTime) -> int:
        sub = defaultdict(list)
        for i,ma in enumerate(manager):
            if ma!=-1: sub[ma].append(i)
        q, t = [(0,headID)], -1
        while q:
            t, x = heapq.heappop(q)
            for y in sub[x]:
                heapq.heappush(q,(t+informTime[x],y))
        return t

    def numOfMinutes2(self, n, headID, manager, informTime) -> int:
        sub = [[] for _ in range(n)]
        for i,ma in enumerate(manager):
            if ma!=-1: sub[ma].append(i)
        def dfs(i):
            if not sub[i]: return 0
            return informTime[i]+max(dfs(x) for x in sub[i])
        return dfs(headID)


a=Solution()
print(a.numOfMinutes(7,6,[1,2,3,4,5,6,-1],[0,6,5,4,3,2,1]))
print(a.numOfMinutes(15,0,[-1,0,0,1,1,2,2,3,3,4,4,5,5,6,6],[1,1,1,1,1,1,1,0,0,0,0,0,0,0,0]))
print(a.numOfMinutes2(7,6,[1,2,3,4,5,6,-1],[0,6,5,4,3,2,1]))
print(a.numOfMinutes2(15,0,[-1,0,0,1,1,2,2,3,3,4,4,5,5,6,6],[1,1,1,1,1,1,1,0,0,0,0,0,0,0,0]))