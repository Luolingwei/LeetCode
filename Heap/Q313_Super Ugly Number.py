# Input: n = 12, primes = [2,7,13,19]
# Output: 32
# Explanation: [1,2,4,7,8,13,14,16,19,26,28,32] is the sequence of the first 12
#              super ugly numbers given primes = [2,7,13,19] of size 4.

#思路 每个ugly number都由某个prime 乘以 已有的ugly number构成, 所以每次pop一个后,只需要在heap中加入对应底数(2,7,13,19)乘的下一个ugly number即可
# 即每次pop的是各个底数构成的最小ugly number中最小的那个,然后补充进对应底数构成的下一个相邻的ugly number

import heapq
class Solution:
    def nthSuperUglyNumber(self, n, primes):
        queue,dp=[],[1]
        for i in range(len(primes)):heapq.heappush(queue,[primes[i],0,primes[i]])
        while len(dp)<n:
            value,i,base=heapq.heappop(queue)
            if value!=dp[-1]: dp+=[value]
            heapq.heappush(queue,[base*dp[i+1],i+1,base])
        return dp[-1]

a=Solution()
print(a.nthSuperUglyNumber(12, [2, 7, 13, 19]))