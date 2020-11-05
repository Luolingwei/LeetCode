
# 思路: 用brick一直往前走, 并用heap记录用过的brick数量
# 当brick不够用的时候(brick<0), 拿出1个ladder替换用过的最大的brick, 继续往前走
# brick不够用且没有ladder时, 结束

import heapq
class Solution:
    def furthestBuilding(self, heights, bricks, ladders):
        pos = 0
        used = []
        while pos < len(heights)-1:
            cost = heights[pos+1] - heights[pos]
            if cost>0:
                bricks -= cost
                heapq.heappush(used, -cost)
                while bricks<0:
                    ladders -= 1
                    if ladders<0: return pos
                    bricks-=heapq.heappop(used)
            pos+=1
        return pos


a=Solution()
print(a.furthestBuilding([4,2,7,6,9,14,12],5,1))
print(a.furthestBuilding([4,12,2,7,3,18,20,3,19],10,2))
print(a.furthestBuilding([14,3,19,3],17,0))