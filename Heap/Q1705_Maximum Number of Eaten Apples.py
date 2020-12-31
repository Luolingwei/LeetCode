import heapq

# 思路: 将apple按照过期时间从小到大加入heap, 每次吃过期时间最近的apple,
# 如果当前apple过期或者吃完, 从heap pop, 吃堆顶的一个apple, 直到所有的apple吃完为止

class Solution:
    def eatenApples(self, apples, days) -> int:
        res, i = 0, 0
        q = []
        while i<len(apples) or q:
            if i<len(apples) and apples[i]>0:
                heapq.heappush(q, [i+days[i],apples[i]])
            while q and (q[0][0]<=i or q[0][1]==0):
                heapq.heappop(q)
            if q:
                q[0][1] -= 1
                res += 1
            i += 1
        return res

a=Solution()
print(a.eatenApples([1,2,3,5,2],[3,2,1,4,2]))
print(a.eatenApples([3,0,0,0,0,2],[3,0,0,0,0,2]))