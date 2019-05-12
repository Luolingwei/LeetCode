# 1. The number at the ith position is divisible by i.
# 2. i is divisible by the number at the ith position.

# Input: 2
# Output: 2
# [1,2] [2,1]

# 思路: BFS, 从N到1分别排数字，可以排的条件为x%i==0 or i%x==0，然后进行递归求count的总数
# Note: 这里很好地使用了Set可以减的性质，对集合进行递减更新

class Solution:
    def countArrangement(self, N):
        def count(i,X):
            if i==1: #第一个位置放什么数字都可以
                return 1
            return sum([count(i-1,X-{x}) for x in X if (x%i==0 or i%x==0)])
        return count(N,set(range(1,N+1)))

a=Solution()
print(a.countArrangement(2))