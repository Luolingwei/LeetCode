import heapq
class Solution:
    # Solution 1: bisect insort
    # def lastStoneWeight(self, stones):
    #     stones.sort()
    #     while len(stones)>=2:
    #         stone1,stone2=stones.pop(),stones.pop()
    #         carry=abs(stone1-stone2)
    #         if carry:
    #             bisect.insort(stones,carry)
    #     return stones[0] if stones else 0

    # Solution 2: heapq
    def lastStoneWeight(self, stones):
        queue=[-stone for stone in stones]
        heapq.heapify(queue)
        while len(queue)>=2:
            stone1,stone2=heapq.heappop(queue),heapq.heappop(queue)
            carry=abs(stone1-stone2)
            if carry:
                heapq.heappush(queue,-carry)
        return -queue[0] if queue else 0

a=Solution()
print(a.lastStoneWeight([2,7,4,1,8,1]))
print(a.lastStoneWeight([2,5,8]))
print(a.lastStoneWeight([2]))
print(a.lastStoneWeight([]))