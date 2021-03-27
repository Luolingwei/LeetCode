import heapq

# 思路1, sorting, 从最大数开始去掉x个, 那么最小数去掉3-x个。得到最大的gap, O(nlogn)
# 思路2: 用heap只记录最大的4个数和最小的4个数，同样的方法得到最大的gap, O(n)

class Solution:
    def minDifference(self, nums):
        if (len(nums)<=4): return 0
        maxHeap, minHeap = [], []
        for n in nums:
            heapq.heappush(maxHeap, n)
            if len(maxHeap)>4: heapq.heappop(maxHeap)
            heapq.heappush(minHeap, -n)
            if len(minHeap)>4: heapq.heappop(minHeap)
        maxQ, minQ = [], []
        while maxHeap: maxQ.append(heapq.heappop(maxHeap))
        while minHeap: minQ.append(-heapq.heappop(minHeap))
        print(maxQ,minQ)
        res = float('inf')
        for x in range(4):
            res = min(res, maxQ[3-x] - minQ[x])
        return res


a=Solution()
print(a.minDifference([1,5,0,10,14]))
print(a.minDifference([9,48,92,48,81,31]))
print(a.minDifference([14,10,5,1,0]))