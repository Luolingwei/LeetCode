# Example 1:
# Input:
# n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
# src = 0, dst = 2, k = 1
# Output: 200

# bfs, TLE. 用heap优化 (Priority Queue)，注意这里和普通bfs以dist为判断标准的区别，这里不是要dist最小，而是要cost最少，所以用heap pop 出当前cost最小的线路. 直到出现dst

import heapq
import collections
class Solution:
    def findCheapestPrice(self, n, flights, src, dst, K):
        dic=collections.defaultdict(dict)
        for s,d,c in flights:
            dic[s][d]=c
        queue=[(0,src,-1)]
        while queue:
            cost,node,stop=heapq.heappop(queue)
            if node==dst: return cost
            if stop<K:
                for nextdst in dic[node]:
                    heapq.heappush(queue,(cost+dic[node][nextdst],nextdst,stop+1))
        return -1

a=Solution()
print(a.findCheapestPrice(3,[[0,1,100],[1,2,100],[0,2,500]],0,2,1))
print(a.findCheapestPrice(3,[[0,1,100],[1,2,100],[0,2,500]],0,2,0))
print(a.findCheapestPrice(5,[[4,1,1],[1,2,3],[0,3,2],[0,4,10],[3,1,1],[1,4,3]],2,1,1))
print(a.findCheapestPrice(5,[[0,1,5],[1,2,5],[0,3,2],[3,1,2],[1,4,1],[4,2,1]],0,2,2))