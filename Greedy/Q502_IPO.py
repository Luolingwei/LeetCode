# Input: k=2, W=0, Profits=[1,2,3], Capital=[0,1,1].
#
# Output: 4
#
# Explanation: Since your initial capital is 0, you can only start the project indexed 0.
#              After finishing it you will obtain profit 1 and your capital becomes 1.
#              With capital 1, you can either start the project indexed 1 or the project indexed 2.
#              Since you can choose at most 2 projects, you need to finish the project indexed 2 to get the maximum capital.
#              Therefore, output the final maximized capital, which is 0 + 1 + 3 = 4.

# 思路: 用heap存储所有符合条件的项目的profit，每次拿profit最大的一个，拿k次.

import heapq
class Solution:
    def findMaximizedCapital(self, k, W, Profits, Capital):
        projects=sorted(zip(Capital,Profits),key=lambda x:x[0])
        i,N,queue=0,len(Profits),[]
        for _ in range(k):
            while i<N and projects[i][0]<=W:
                heapq.heappush(queue,-projects[i][1])
                i+=1
            if queue: W-=heapq.heappop(queue)
        return W

a=Solution()
print(a.findMaximizedCapital(2,0,[1,2,3],[0,1,1]))
print(a.findMaximizedCapital(1,0,[1,2,3],[1,1,2]))