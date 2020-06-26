import bisect

# 思路: 遇到0(不下雨)将index加入slots中, 遇到下雨, 用map记录 {lake: rainday}
# 如果碰到map中已有的key，说明之前的lake需要清理, 用slots中比rainday大的slot清理
# 用bisect求得比rainday大一点点的slot, 并从slot中pop, 如果没有说明失败, 返回[]
# 如果用Java TreeSet则可以将slots用TreeSet记录, 每次查出比rainday大一点的slot, remove(O(1)), 则为O(nlogn)

class Solution:
    def avoidFlood(self, rains):
        res = [-1]*len(rains)
        slots = []
        memo = {}
        for i,r in enumerate(rains):
            if r==0:
                slots.append(i)
            else:
                if r in memo:
                    idx = bisect.bisect_left(slots,memo[r])
                    if idx == len(slots): return []
                    res[slots.pop(idx)] = r
                memo[r] = i
        while slots:
            res[slots.pop()] = 1
        return res


a=Solution()
print(a.avoidFlood([1,2,3,4]))
print(a.avoidFlood([1,2,0,0,2,1]))
print(a.avoidFlood([1,2,0,1,2]))
print(a.avoidFlood([69,0,0,0,69]))
print(a.avoidFlood([10,20,20]))