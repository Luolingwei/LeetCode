# Input: A = [1,1], B = [2,2]
# Output: [1,2]

# 思路: 先计算gap，然后寻找可以交换的pair

class Solution:
    def fairCandySwap(self, A, B):
        gap=(sum(A)-sum(B))//2
        B=set(B)
        for a in set(A):
            if a-gap in B: return [a,a-gap]

a=Solution()
print(a.fairCandySwap([1,2,5],[2,4]))