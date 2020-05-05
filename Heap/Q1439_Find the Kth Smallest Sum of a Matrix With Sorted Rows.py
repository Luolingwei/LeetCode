
# 思路: 每次pop出当前最小的s, 然后需要将接下来可能成为ans的candidate放进heap
# 即每个位置向后移动一位, 注意可能产生重复, 所以用memo记录index集合去重

import heapq
class Solution:
    def kthSmallest(self, mat, k: int) -> int:
        m, n = len(mat), len(mat[0])
        s = sum(mat[i][0] for i in range(m))
        queue = [[s, [0]*m]]
        memo = set()
        for _ in range(k):
            s, q = heapq.heappop(queue)
            for j, idx in enumerate(q):
                if idx + 1 < n:
                    tempq = q[:]
                    tempq[j] += 1
                    if str(tempq) not in memo:
                        temps = s + (mat[j][tempq[j]] - mat[j][tempq[j] - 1])
                        heapq.heappush(queue, [temps, tempq])
                        memo.add(str(tempq))
        return s

a=Solution()
print(a.kthSmallest([[1,3,11],[2,4,6]],5))
print(a.kthSmallest([[1,3,11],[2,4,6]],9))
print(a.kthSmallest([[1,10,10],[1,4,5],[2,3,6]],7))
print(a.kthSmallest([[1,1,10],[2,2,9]],7))