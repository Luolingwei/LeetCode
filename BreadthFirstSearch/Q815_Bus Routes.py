# Example:
# Input:
# routes = [[1, 2, 7], [3, 6, 7]]
# S = 1
# T = 6
# Output: 2
# Explanation:
# The best strategy is take the first bus to the bus stop 7, then take the second bus to the bus stop 6.

# 思路: bfs, 以line为bfs的对象，每次根据当前能到达的line加入所有的stop, 用visited记录已经访问的line
# queue中存储的为 换乘1,2,3,4,5.....次line的(count,stop), 遇到T则返回count

import collections
class Solution:
    def numBusesToDestination(self, routes, S, T):
        stop2route=collections.defaultdict(set)
        for line, stops in enumerate(routes):
            for stop in stops:
                stop2route[stop].add(line)
        queue,visited=[(0,S)],set()
        while queue:
            count,stop=queue.pop(0)
            if stop==T: return count
            for line in stop2route[stop]:
                if line not in visited:
                    queue+=[(count+1,stop) for stop in routes[line]]
                visited.add(line)
        return -1

a=Solution()
print(a.numBusesToDestination([[1, 2, 7], [3, 6, 7]],1,6))