import heapq
class Solution:
    # Solution 1 dp
    def nthUglyNumber(self, n):
        table=[1]*n
        i2=i3=i5=0
        for i in range(1,n):
            table[i]=min(table[i2]*2,table[i3]*3,table[i5]*5)
            if table[i]==table[i2]*2:
                i2+=1
            if table[i]==table[i3]*3:
                i3+=1
            if table[i]==table[i5]*5:
                i5+=1
        return table[-1]

    # Solution 2 heap
    # def nthUglyNumber(self, n):
    #     queue = [1]
    #     visited = set()
    #     for _ in range(n):
    #         x = heapq.heappop(queue)
    #         for i in [2, 3, 5]:
    #             if x * i not in visited:
    #                 heapq.heappush(queue, x * i)
    #                 visited.add(x * i)
    #     return x

a=Solution()
print(a.nthUglyNumber(10))