
import heapq

# 思路: 所有的数从最小的值开始加入pq, 然后增加最小的数(*2, 条件是这个数小于原数/这个数是奇数), 更新max-min的最小值
# 终止条件是pq中有数出局(长度变小), 即最小数已经确定, 停止循环

class Solution:
    def minimumDeviation(self, nums):
        def get_min_odd(n):
            while n&1==0:
                n>>=1
            return n
        q = [[get_min_odd(n),n] for n in nums]
        heapq.heapify(q)
        res, maxN = float('inf'), max([a for a,a0 in q])
        while len(q)==len(nums):
            a, a0 = heapq.heappop(q)
            res = min(res, maxN-a)
            if a%2!=0 or a<a0:
                maxN = max(maxN, a*2)
                heapq.heappush(q, [a*2, a0])
        return res


a=Solution()
print(a.minimumDeviation([1,2,3,4]))
print(a.minimumDeviation([4,1,5,20,3]))
print(a.minimumDeviation([2,10,8]))
print(a.minimumDeviation([10,4,3]))
print(a.minimumDeviation([3,5]))