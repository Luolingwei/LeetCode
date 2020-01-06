
# 思路: 从第一个人开始assign bike，用mask记录已经take的bikes，每个人选的时候可以选没有被take的bike，加入heap
# 每次pop当前cost最小的组合，直到i达到len(workers)
# 注意用visited记录已经访问过的 (curtaken,curi)的组合(已经有更优cost)，减少重复搜索

import heapq
class Solution:
    def assignBikes(self, workers, bikes):
        def dist(i, j):
            return abs(workers[i][0] - bikes[j][0]) + abs(workers[i][1] - bikes[j][1])
        q, visited, M, N = [], set(), len(workers), len(bikes)
        heapq.heappush(q, (0, 0, 0))
        while True:
            curcost, curtaken, curi = heapq.heappop(q)
            if (curtaken, curi) in visited:
                continue
            visited.add((curtaken, curi))
            if curi == M: return curcost
            for j in range(N):
                if curtaken & (1 << j) == 0:
                    heapq.heappush(q, (curcost + dist(curi, j), curtaken | (1 << j), curi + 1))

a=Solution()
print(a.assignBikes([[0,0],[1,1],[2,0]],[[1,0],[2,2],[2,1]]))