import heapq

# 思路: 反向每次将最大值减去剩下的总和，如果某次减去后小于1，则不成功
# 停止条件为curS=len，即每个元素都为1
# 用heap每次pop出最大的数，变换后pop回去，动态记录curS

class Solution:
    def isPossible(self, target):
        des=len(target)
        curS=sum(target)
        target=[-n for n in target]
        heapq.heapify(target)
        while curS>des:
            maxN=-heapq.heappop(target)
            minus=curS-maxN
            maxN-=minus
            curS-=minus
            if maxN<1: return False
            heapq.heappush(target,-maxN)
        return True

a=Solution()
print(a.isPossible([9,3,5]))
print(a.isPossible([1,1,1,2]))
print(a.isPossible([8,5]))